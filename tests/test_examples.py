"""Test the examples in ``../examples``."""

import clack.cli

import pytest


def test_farm(run_example):
    assert run_example('farm').exit_code == 0


def test_hello(run_example):
    assert run_example('hello').exit_code == 0
