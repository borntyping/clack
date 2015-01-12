"""Test the examples in ``../examples``."""

import subprocess

import clack.cli

import pytest


COWSAY_AVAILIBLE = bool(subprocess.call('which cowsay', shell=True))


@pytest.mark.skipif(COWSAY_AVAILIBLE, reason="cowsay is not installed")
def test_farm_json(run_example):
    assert run_example('farm.json').exit_code == 0


@pytest.mark.skipif(COWSAY_AVAILIBLE, reason="cowsay is not installed")
def test_farm_yaml(run_example):
    assert run_example('farm.yaml').exit_code == 0


def test_hello(run_example):
    assert run_example('hello.json').exit_code == 0
