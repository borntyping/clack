"""Command Line Accessible Calling Kit"""

__version__ = '0.0.0'
__author__ = 'Sam Clements <sam@borntyping.co.uk>'

import clack.callable


def prepare(*args, **kwargs):
    return clack.callable.Callable(*args, **kwargs)


def call(*args, **kwargs):
    return clack.callable.Callable(*args, **kwargs).run()
