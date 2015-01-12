"""Test the examples in ``../examples``."""

import subprocess

import clack.cli

import pytest


@pytest.mark.skipif(
    subprocess.call('which cowsay', shell=True),
    reason="cowsay is not installed")
def test_farm(run_example):
    assert run_example('farm').exit_code == 0


def test_hello(run_example):
    assert run_example('hello').exit_code == 0
