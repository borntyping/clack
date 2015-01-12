=====
clack
=====

.. image:: http://img.shields.io/pypi/v/clack.svg?style=flat-square
    :target: https://pypi.python.org/pypi/clack
    :alt: clack on PyPI

.. image:: http://img.shields.io/pypi/l/clack.svg?style=flat-square
    :target: https://pypi.python.org/pypi/clack
    :alt: clack on PyPI

.. image:: https://readthedocs.org/projects/clack/badge/?version=latest&style=flat-square
    :target: http://clack.readthedocs.org/en/latest/
    :alt: Documentation for clack on Read The Docs

.. image:: http://img.shields.io/travis/borntyping/clack/master.svg?style=flat-square
    :target: https://travis-ci.org/borntyping/clack
    :alt: Travis-CI build status for clack

.. image:: https://img.shields.io/github/issues/borntyping/clack.svg?style=flat-square
    :target: https://github.com/borntyping/clack/issues
    :alt: GitHub issues for clack

|

Run multiple iterations of the same command from a stored configuration.

I build this to help with building multiple packages using fpm_. I had a set of commands where it was useful to share default and common arguments for each package, and the commands were complex enough that I wanted a configuration file describing them (and generic functions are *painful* in make). An example of using clack with fpm_ can be found in ``examples/fpm.json``.

* `Source on GitHub <https://github.com/borntyping/python-clack>`_
* `Documentation on Read the Docs <http://clack.readthedocs.org/en/latest/>`_
* `Packages on PyPI <https://pypi.python.org/pypi/clack>`_

Usage
-----

Create a configuration file:

.. code:: json

    {
        "default": {
            "command": "cowsay",
            "options": { "-f": "default" }
        },
        "iterations": [
            {
                "arguments": ["moo"]
            },
            {
                "arguments": ["baa"],
                "options": { "-f": "sheep" }
            }
        ]
    }

Then run clack on the file:

.. code:: bash

    clack examples/farm.json

And the result:

.. code::
     _____
    < moo >
     -----
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
     _____
    < baa >
     -----
      \
       \
           __
          UooU\.'@@@@@@`.
          \__/(@@@@@@@@@@)
               (@@@@@@@@)
               `YY~~~~YY'
                ||    ||


Installation
------------

Install clack with pip_ or pipsi_.

.. code:: bash

    pip install clack

Licence
-------

``clack`` is licensed under the `MIT Licence <http://opensource.org/licenses/MIT>`_.

Authors
-------

``clack`` was written by `Sam Clements <https://github.com/borntyping>`_.

.. _fpm: https://github.com/jordansissel/fpm
.. _pip: http://pip.readthedocs.org/en/stable/
.. _pipsi: https://github.com/mitsuhiko/pipsi
