"""Behave environment hooks for Almanac BDD tests."""

from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path


def before_all(context):
    """Setup global test environment."""
    # Find repo root
    context.repo_root = Path(__file__).resolve().parents[4]
    context.almanac_root = context.repo_root


def before_scenario(context, scenario):
    """Setup isolated environment for each scenario."""
    # Create a temporary directory for the almanac
    context.tmp_dir = Path(tempfile.mkdtemp(prefix="almanac-bdd-"))
    context.tmp_almanac = context.tmp_dir / "almanac"
    context.tmp_almanac.mkdir()

    # Create minimal structure
    (context.tmp_almanac / "SCHEMA.md").write_text("# Schema")
    (context.tmp_almanac / "AREAS.md").write_text("# Areas")
    (context.tmp_almanac / "areas").mkdir()
    (context.tmp_almanac / "authors").mkdir()
    (context.tmp_almanac / "guides").mkdir()
    (context.tmp_almanac / "meta").mkdir()

    # Copy areas.yml if it exists
    src_config = context.almanac_root / "meta" / "areas.yml"
    if src_config.exists():
        shutil.copy(src_config, context.tmp_almanac / "meta" / "areas.yml")

    context.last_command = None


def after_scenario(context, scenario):
    """Cleanup temporary directory."""
    if hasattr(context, "tmp_dir") and context.tmp_dir.exists():
        shutil.rmtree(context.tmp_dir)
