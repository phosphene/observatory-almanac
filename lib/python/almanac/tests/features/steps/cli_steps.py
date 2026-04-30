"""Step definitions for Almanac CLI BDD tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from behave import given, then, when


def _run_cli(context, cmd: str, extra_args: list[str] | None = None) -> None:
    """Run an almanac CLI subcommand against the temp almanac root.

    Args:
        context: Behave context carrying tmp_almanac path.
        cmd: Subcommand name (e.g. 'validate', 'index', 'tree').
        extra_args: Additional CLI args to append.
    """
    args = extra_args or []
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            f"from almanac.cli import main; import sys; "
            f"sys.exit(main(['{cmd}', '--root', '{context.tmp_almanac}'] + {args!r}))",
        ],
        capture_output=True,
        text=True,
    )
    context.last_command = result


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


@given("the author profile contains a link to a missing article")
def step_impl(context):
    """Append a broken article link to the last-created author profile.

    Writes a link pointing to a path that does not exist in the almanac,
    simulating an author profile referencing an unpublished article.
    """
    profile = context.tmp_almanac / "authors" / "missing-article-author.md"
    profile.parent.mkdir(parents=True, exist_ok=True)
    profile.write_text(
        "---\nname: missing-article-author\nslug: missing-article-author\n---\n\n"
        "## Articles\n\n"
        "- [The Vanished Article](../areas/science/vanished-article.md) — Science\n",
        encoding="utf-8",
    )


@when("I run the task generator")
def step_impl(context):
    """Execute the almanac tasks CLI subcommand."""
    _run_cli(context, "tasks")


@when("I run the validator")
def step_impl(context):
    """Execute the almanac validate CLI subcommand."""
    _run_cli(context, "validate")


@when('I run the indexer')
def step_impl(context):
    """Execute the almanac index CLI subcommand."""
    _run_cli(context, "index")


@when('I run the indexer with "{flags}"')
def step_impl(context, flags):
    """Execute the almanac index CLI subcommand with extra flags."""
    extra = flags.split()
    _run_cli(context, "index", extra)


@when('I run the tree builder')
def step_impl(context):
    """Execute the almanac tree CLI subcommand."""
    _run_cli(context, "tree")


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


@then('the file "{path}" should exist')
def step_impl(context, path):
    """Verify that a file exists in the temp almanac."""
    target = context.tmp_almanac / path
    assert target.exists(), f"Expected file {path} to exist, but it does not"


@then('the file "{path}" should not exist')
def step_impl(context, path):
    """Verify that a file does not exist in the temp almanac."""
    target = context.tmp_almanac / path
    assert not target.exists(), f"Expected file {path} to not exist, but it does"


@then('the file "{path}" should contain "{text}"')
def step_impl(context, path, text):
    """Verify that a file contains specific text."""
    target = context.tmp_almanac / path
    assert target.exists(), f"File {path} does not exist"
    content = target.read_text(encoding="utf-8")
    assert text in content, f"Could not find '{text}' in {path}:\n{content[:500]}"


@then('the file "{path}" should not contain "{text}"')
def step_impl(context, path, text):
    """Verify that a file does not contain specific text."""
    target = context.tmp_almanac / path
    assert target.exists(), f"File {path} does not exist"
    content = target.read_text(encoding="utf-8")
    assert text not in content, (
        f"Expected '{text}' to be absent from {path}, but it was found"
    )


@then('the stdout should not contain "{text}"')
def step_impl(context, text):
    """Verify that stdout does not contain specific text."""
    assert text not in context.last_command.stdout, (
        f"Expected '{text}' to be absent from stdout, but it was found:\n"
        f"{context.last_command.stdout[:500]}"
    )


@then('the stderr should not contain "{text}"')
def step_impl(context, text):
    """Verify that stderr does not contain specific text."""
    assert text not in context.last_command.stderr, (
        f"Expected '{text}' to be absent from stderr, but it was found:\n"
        f"{context.last_command.stderr[:500]}"
    )
