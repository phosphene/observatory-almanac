"""Unified CLI orchestration for the Observatory Almanac.

Provides entry points for validation, indexing, and documentation tree
generation.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from almanac.io import find_root


def validator_main(argv: list[str] | None = None) -> int:
    """CLI entry point for content validation."""
    from almanac.validator import run_validation

    p = argparse.ArgumentParser(
        description="Validate Observatory Almanac content against SCHEMA.md"
    )
    p.add_argument(
        "--root", type=Path, default=None, help="Almanac root (auto-detected)"
    )
    p.add_argument("--verbose", action="store_true", help="Print valid files to stderr")
    args = p.parse_args(argv)

    try:
        root = args.root.resolve() if args.root else find_root()
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    return run_validation(root, verbose=args.verbose)


def indexer_main(argv: list[str] | None = None) -> int:
    """CLI entry point for the index and index-page generator."""
    from almanac.index import run as run_inventory
    from almanac.indexing import run as run_area_indices

    p = argparse.ArgumentParser(description="Generate Observatory Almanac indices")
    p.add_argument(
        "--root", type=Path, default=None, help="Almanac root (auto-detected)"
    )
    p.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = p.parse_args(argv)

    try:
        root = args.root.resolve() if args.root else find_root()
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    # 1. Regenerate meta/index.md and meta/CONTEXT_INDEX.md
    res = run_inventory(root, dry_run=args.dry_run)
    if res != 0:
        return res

    # 2. Regenerate per-area index.md pages
    run_area_indices(root, dry_run=args.dry_run)
    return 0


def tree_main(argv: list[str] | None = None) -> int:
    """CLI entry point for MkDocs symlink tree generation."""
    from almanac.docs_tree import build_docs_tree

    p = argparse.ArgumentParser(description="Build MkDocs symlink tree")
    p.add_argument(
        "--root", type=Path, default=None, help="Almanac root (auto-detected)"
    )
    args = p.parse_args(argv)

    try:
        root = args.root.resolve() if args.root else find_root()
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    try:
        build_docs_tree(root)
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


def main(argv: list[str] | None = None) -> int:
    """Unified entry point dispatcher."""
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print("Usage: almanac <command> [options]")
        print("Commands: validate, index, tree")
        return 1

    cmd = argv[0]
    args = argv[1:]

    if cmd == "validate":
        return validator_main(args)
    if cmd == "index":
        return indexer_main(args)
    if cmd == "tree":
        return tree_main(args)

    print(f"Unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
