"""Test the CLI directly."""

import json

import clack.cli

import click.testing
import pytest


@pytest.yield_fixture
def example_runner():
    runner = click.testing.CliRunner()
    with runner.isolated_filesystem():
        with open('example.json', 'w') as f:
            json.dump({
                "default": {
                    "command": "echo"
                },
                "iterations": [
                    { "arguments": ["hello"] },
                    { "arguments": ["world"] }
                ]
            }, f)
        yield runner


def test_success(example_runner):
    result = example_runner.invoke(clack.cli.main, ['example.json'])
    assert result.exit_code == 0


def test_output(example_runner, capfd):
    example_runner.invoke(clack.cli.main, ['example.json'])
    # Use py.test capsys to read STDOUT, since it's subprocesses are
    # actually printing output
    out, err = capfd.readouterr()
    assert 'hello' in out
    assert 'world' in out
