"""Isolated filesystem operations for the Observatory Almanac.

Decouples core logic from I/O by providing a stable interface for
reading content, writing artifacts, and managing symlinks.
"""

from __future__ import annotations

import sys
from pathlib import Path


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


def read_text(path: Path) -> str:
    """Read UTF-8 text from a file.

    Args:
        path: Path to the file.

    Returns:
        File contents as a string.

    Raises:
        OSError: If the file cannot be read.
    """
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    """Write UTF-8 text to a file, creating parent directories if needed.

    Args:
        path: Path to the target file.
        content: Text to write.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_symlink(src: Path, dst: Path) -> None:
    """Create an idempotent symlink.

    If a symlink or file already exists at ``dst``, it is unlinked before
    the new symlink is created.

    Args:
        src: Source path (what the link points to).
        dst: Destination path (the link itself).
    """
    if dst.is_symlink() or dst.exists():
        dst.unlink()
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.symlink_to(src.resolve())


def find_root(start_path: Path | None = None) -> Path:
    """Locate the almanac repo root by walking up from start_path.

    Root is identified by the presence of ``SCHEMA.md`` and ``AREAS.md``.

    Args:
        start_path: Path to start searching from (defaults to CWD).

    Returns:
        Absolute path to the repository root.

    Raises:
        RuntimeError: If the root cannot be located.
    """
    curr = (start_path or Path.cwd()).resolve()
    for candidate in [curr, *curr.parents]:
        if (candidate / "SCHEMA.md").exists() and (candidate / "AREAS.md").exists():
            return candidate
    raise RuntimeError(
        "Could not locate almanac root (expected 'SCHEMA.md' and 'AREAS.md')."
    )
