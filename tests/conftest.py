import clack.cli

import click.testing
import pytest


@pytest.fixture
def run():
    return lambda *a: click.testing.CliRunner().invoke(clack.cli.main, a)


@pytest.fixture
def run_example(run):
    return lambda example: run('examples/{0}.json'.format(example))
