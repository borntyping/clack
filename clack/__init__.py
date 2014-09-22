"""A tool for executing multiple commands from a data file"""

__version__ = '0.1.0'
__author__ = 'Sam Clements <sam@borntyping.co.uk>'

import clack.callable


def prepare(*args, **kwargs):
    return clack.callable.Callable(*args, **kwargs)


def call(*args, **kwargs):
    return clack.callable.Callable(*args, **kwargs).run()
