"""Utility functions for clack."""

import os.path
import sys

__all__ = ('local_path', 'string_types')


def local_path(filename):
    """Return an absolute path to a file in the current directory."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


if sys.version_info >= (3,):
    string_types = (str,)
else:
    string_types = (basestring,)
