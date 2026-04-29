"""Step definitions for Almanac CLI BDD tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from behave import given, then, when


@given('an area "{area}" exists')
def step_impl(context, area):
    """Ensure an area directory exists in the mock almanac."""
    (context.tmp_almanac / "areas" / area).mkdir(parents=True, exist_ok=True)


@given('a document "{path}" with:')
def step_impl(context, path):
    """Create a document with specific content."""
    p = context.tmp_almanac / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(context.text, encoding="utf-8")


@given('an author profile "{path}" exists')
def step_impl(context, path):
    """Create a minimal author profile."""
    p = context.tmp_almanac / path
    p.parent.mkdir(parents=True, exist_ok=True)
    slug = Path(path).stem
    p.write_text(f"---\nname: Test Author\nslug: {slug}\n---", encoding="utf-8")


@when("I run the validator")
def step_impl(context):
    """Execute the almanac-validator CLI tool."""
    cmd = [
        sys.executable,
        "-m",
        "almanac.cli",
        "validate",  # I'll update cli.py to support subcommands if needed, or use the direct entry point
        "--root",
        str(context.tmp_almanac),
    ]
    # Actually, I named them almanac-validator etc. in pyproject.toml
    # But for BDD I can just call the functions directly or use subprocess on the module
    # Let's use subprocess on the module to be safe and independent
    result = subprocess.run(
        [sys.executable, "-c", f"from almanac.cli import validator_main; import sys; sys.exit(validator_main(['--root', '{context.tmp_almanac}']))"],
        capture_output=True,
        text=True,
    )
    context.last_command = result


@then("the exit code should be {code:d}")
def step_impl(context, code):
    """Verify the exit code of the last command."""
    if context.last_command.returncode != code:
        print(f"STDOUT: {context.last_command.stdout}")
        print(f"STDERR: {context.last_command.stderr}")
    assert context.last_command.returncode == code, f"Expected {code}, got {context.last_command.returncode}"


@then('the stderr should contain "{text}"')
def step_impl(context, text):
    """Verify that stderr contains specific text."""
    assert text in context.last_command.stderr, f"Could not find '{text}' in stderr: {context.last_command.stderr}"


@then('the stdout should contain "{text}"')
def step_impl(context, text):
    """Verify that stdout contains specific text."""
    assert text in context.last_command.stdout, f"Could not find '{text}' in stdout: {context.last_command.stdout}"
