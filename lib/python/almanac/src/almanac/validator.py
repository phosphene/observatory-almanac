"""Content validation for the Observatory Almanac.

Walks the almanac content tree and validates every document against its
corresponding Pydantic schema model.  Reports violations to stderr and
returns a non-zero exit code for CI integration.

Exit codes
----------
0 — All documents valid.
1 — One or more validation errors found.
2 — Fatal error (e.g. repository root not found, YAML parse failure).

stdout / stderr split
---------------------
``stdout`` emits only the structured violation report (YAML list).
``stderr`` emits progress messages and a human-readable summary.
This allows downstream tools to parse stdout without noise.

Design note
-----------
The validator does NOT repair documents — it reports violations and exits.
Repair is the scraper's responsibility.  This separation keeps the validator
predictable: it is a pure read operation with no side effects.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import NamedTuple

from pydantic import ValidationError

from almanac.parsing import split_frontmatter
from almanac.schema import parse_frontmatter

# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


class Violation(NamedTuple):
    """A single schema violation detected during validation.

    Attributes:
        path: Relative path to the offending file.
        field: Field name where the violation occurred, or 'frontmatter'
            for structural parse failures.
        message: Human-readable description of the violation.
    """

    path: str
    field: str
    message: str


# ---------------------------------------------------------------------------
# Logic layer (pure — no filesystem writes, no printing)
# ---------------------------------------------------------------------------


def extract_frontmatter_yaml(text: str) -> tuple[dict, str]:
    """Split a markdown document into frontmatter dict and body.

    Thin wrapper over ``almanac.parsing.split_frontmatter`` that adapts
    its error messages to the validator's expected vocabulary.  The
    canonical implementation lives in ``almanac.parsing``; this function
    exists only to avoid breaking callers inside the validator module.

    Args:
        text: Full document text including ``---`` delimiters.

    Returns:
        Tuple of (frontmatter_dict, body_text).

    Raises:
        ValueError: If no valid frontmatter block is found or is malformed.
    """
    if not text.startswith("---"):
        raise ValueError("No frontmatter block found (document must start with ---)")
    try:
        return split_frontmatter(text)
    except ValueError as exc:
        raise ValueError(
            f"Frontmatter block not closed (missing closing ---): {exc}"
        ) from exc


def validate_document(path: Path, root: Path) -> list[Violation]:
    """Validate a single content file against its schema model.

    Args:
        path: Absolute path to the content file.
        root: Almanac repository root (for relative path reporting).

    Returns:
        List of ``Violation`` instances; empty list means the document is valid.
    """
    rel = str(path.relative_to(root))
    violations: list[Violation] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        violations.append(Violation(rel, "io", str(exc)))
        return violations

    try:
        data, _ = extract_frontmatter_yaml(text)
    except ValueError as exc:
        violations.append(Violation(rel, "frontmatter", str(exc)))
        return violations

    try:
        parse_frontmatter(data)
    except ValidationError as exc:
        for err in exc.errors():
            field = ".".join(str(loc) for loc in err["loc"])
            violations.append(Violation(rel, field, err["msg"]))
    except (ValueError, TypeError) as exc:
        violations.append(Violation(rel, "schema", str(exc)))

    return violations


def validate_author_refs(root: Path) -> list[Violation]:
    """Verify that every author_slug in articles has a matching author profile.

    Args:
        root: Almanac repository root.

    Returns:
        List of referential integrity violations.
    """
    authors_dir = root / "authors"
    known_slugs = (
        {p.stem for p in authors_dir.glob("*.md")} if authors_dir.exists() else set()
    )

    violations: list[Violation] = []
    areas_dir = root / "areas"
    if not areas_dir.exists():
        return violations

    for md_file in sorted(areas_dir.rglob("*.md")):
        try:
            text = md_file.read_text(encoding="utf-8")
            data, _ = extract_frontmatter_yaml(text)
        except (OSError, ValueError):
            continue

        author_slug = data.get("author_slug")
        if (
            author_slug
            and author_slug not in known_slugs
            and author_slug != "the-observatory"
        ):
            violations.append(
                Violation(
                    str(md_file.relative_to(root)),
                    "author_slug",
                    f"No matching profile in authors/{author_slug}.md",
                )
            )

    return violations


# ---------------------------------------------------------------------------
# I/O layer
# ---------------------------------------------------------------------------


def collect_content_files(root: Path) -> list[Path]:
    """Enumerate all content markdown files in the almanac.

    Includes ``areas/``, ``guides/``, and ``authors/`` directories.
    Excludes ``meta/``, ``lib/``, ``scripts/``, and ``docs/``.

    Args:
        root: Almanac repository root.

    Returns:
        Sorted list of absolute paths to content files.
    """
    paths: list[Path] = []
    for subdir in ("areas", "guides", "authors"):
        d = root / subdir
        if d.exists():
            paths.extend(sorted(d.rglob("*.md")))
    return paths


def run_validation(root: Path, verbose: bool = False) -> int:
    """Run validation across the full content tree.

    Prints a structured violation report to stdout (YAML list) and a
    human-readable summary to stderr.

    Args:
        root: Almanac repository root.
        verbose: If True, also print valid file names to stderr.

    Returns:
        Exit code: 0 for clean, 1 for violations, 2 for fatal error.
    """
    files = collect_content_files(root)
    if not files:
        print("No content files found. Check repository root.", file=sys.stderr)
        return 2

    all_violations: list[Violation] = []
    for f in files:
        v = validate_document(f, root)
        all_violations.extend(v)
        if verbose and not v:
            print(f"  OK  {f.relative_to(root)}", file=sys.stderr)

    # Author reference check
    all_violations.extend(validate_author_refs(root))

    # Structured stdout output
    if all_violations:
        for v in all_violations:
            print(f"- path: {v.path}", flush=True)
            print(f"  field: {v.field}")
            print(f"  message: {v.message}")

    # Summary to stderr
    print(
        f"\nValidated {len(files)} files — {len(all_violations)} violation(s) found.",
        file=sys.stderr,
    )

    return 0 if not all_violations else 1


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for the content validator.

    Args:
        argv: Argument list (defaults to sys.argv).

    Returns:
        Exit code.
    """
    import argparse

    p = argparse.ArgumentParser(
        description="Validate Observatory Almanac content against SCHEMA.md"
    )
    p.add_argument(
        "--root", type=Path, default=Path("."), help="Almanac root directory"
    )
    p.add_argument("--verbose", action="store_true", help="Print valid files to stderr")
    args = p.parse_args(argv)

    root = args.root.resolve()
    if not (root / "SCHEMA.md").exists():
        print(
            f"SCHEMA.md not found at {root}. Run from the almanac root.",
            file=sys.stderr,
        )
        return 2

    return run_validation(root, verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
