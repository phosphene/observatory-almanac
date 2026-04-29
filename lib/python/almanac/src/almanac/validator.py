"""Content validation for the Observatory Almanac.

Walks the almanac content tree and validates every document against its
corresponding Pydantic schema model.  Reports violations to stderr and
returns a non-zero exit code for CI integration.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import NamedTuple

from pydantic import ValidationError

from almanac.io import collect_content_files, read_text
from almanac.parsing import split_frontmatter
from almanac.schema import parse_frontmatter


class Violation(NamedTuple):
    """A single schema violation detected during validation."""

    path: str
    field: str
    message: str


def validate_document(path: Path, root: Path) -> list[Violation]:
    """Validate a single content file against its schema model."""
    rel = str(path.relative_to(root))
    violations: list[Violation] = []

    try:
        text = read_text(path)
    except OSError as exc:
        violations.append(Violation(rel, "io", str(exc)))
        return violations

    try:
        data, _ = split_frontmatter(text)
        if not text.startswith("---"):
            raise ValueError("No frontmatter block found")
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
    """Verify that every author_slug in articles has a matching author profile."""
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
            text = read_text(md_file)
            data, _ = split_frontmatter(text)
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


def run_validation(root: Path, verbose: bool = False) -> int:
    """Run validation across the full content tree."""
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

    all_violations.extend(validate_author_refs(root))

    if all_violations:
        for v in all_violations:
            print(f"- path: {v.path}", flush=True)
            print(f"  field: {v.field}")
            print(f"  message: {v.message}")

    print(
        f"\nValidated {len(files)} files — {len(all_violations)} violation(s) found.",
        file=sys.stderr,
    )

    return 0 if not all_violations else 1
