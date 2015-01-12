import setuptools

setuptools.setup(
    name='clack',
    version='1.0.0-dev',

    author="Sam Clements",
    author_email="sam@borntyping.co.uk",

    url="https://github.com/borntyping/clack",
    description="Run multiple iterations of commands from a config file",
    long_description=open('README.rst').read(),
    license="MIT",

    packages=setuptools.find_packages(),

    install_requires=[
        'click'
    ],

    entry_points={
        'console_scripts': [
            'clack = clack.command:main',
        ]
    },

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
