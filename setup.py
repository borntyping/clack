#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='clack',
    version='0.0.0-dev',

    author="Sam Clements",
    author_email="sam.clements@datasift.com",

    url="https://github.com/borntyping/python-clack",
    description="Command Line Accessible Calling Kit",
    long_description=open('README.rst').read(),
    license="MIT",

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries'
    ],
)
