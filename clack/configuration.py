"""Configuration for clack - schema, data structures and run methods."""

from __future__ import print_function

import subprocess

import yaml
import jsonschema

import clack.utils


with open(clack.utils.local_path('schema.json')) as f:
    SCHEMA = yaml.load(f)


class Command(object):
    """Represents a command that can be run.

    Options are a dict/map and can be merged. Arguments are a list and are not
    merged. The command, options and arguments are used to create a list of
    arguments to pass to ``subprocess.call``, which should directly avoid
    string quoting issues. The description is only used when ``announce()`` is
    called.
    """

    @classmethod
    def from_json(cls, data):
        """Create a class instance from JSON or a dictionary."""
        # Set default values for essential attributes
        data.setdefault('command', None)
        data.setdefault('options', {})
        data.setdefault('arguments', [])

        # Some JSON attributes can be either a string or a list, but are always
        # transformed into a list by splitting strings on spaces
        data['arguments'] = cls.from_json_str_or_list(data['arguments'])

        return cls(**data)

    @staticmethod
    def from_json_str_or_list(value):
        """Modify a key to ensure it is a list"""
        if isinstance(value, clack.utils.string_types):
            value = value.split(' ')
        return value

    @classmethod
    def merge(cls, a, b):
        """
        Return a new Command instance merging the given Commands.

        The first ``Command`` passed to this function takes precedence.
        Attributes are merged based on the first "truthy" value, with the
        exception of options which are merged as a dictionary.
        """
        return cls(
            command=cls.merge_default(a.command, b.command),
            options=cls.merge_options(a.options, b.options),
            arguments=cls.merge_default(a.arguments, b.arguments, default=[]),
            description=cls.merge_default(a.description, b.description))

    @staticmethod
    def merge_default(*args, **kwargs):
        """Return the first "truthy" value from a series, or a default."""
        for value in args:
            if value:
                return value
        return kwargs.get("default")

    @staticmethod
    def merge_options(*options):
        """Merge a series of dictionaries, earlier values take precedence."""
        result = {}
        for d in options:
            for k, v in d.items():
                result.setdefault(k, v)
        return result

    def __init__(self, command, options, arguments, description=None):
        self.command = command
        self.options = options
        self.arguments = arguments
        self.description = description

    def __str__(self):
        return ' '.join(self.args)

    def __repr__(self):
        return '<{c}: {a!r}>'.format(c=self.__class__.__name__, a=self.args)

    @property
    def args(self):
        """Return a list of the commands arguments."""
        arguments = [self.command]
        for k, v in self.options.items():
            arguments.append(k)
            arguments.append(v)
        for a in self.arguments:
            arguments.append(a)
        return arguments

    def announce(self):
        """Announce the command by printing a message.

        Prints something like this::

            # Description
            $ command --and arguments
        """
        if self.description is not None:
            print("#", self.description)
        print("$", self)

    def run(self):
        """Run the command."""
        assert self.command is not None, "No command is set!"
        subprocess.check_call(self.args)


class Configuration(object):
    """Represents an entire configuration."""

    @classmethod
    def load(cls, path, schema=SCHEMA):
        """Load and validate a configuration from a JSON file."""
        with open(path, 'r') as f:
            data = yaml.load(f)
        jsonschema.validate(data, schema)
        return cls.from_json(data)

    @classmethod
    def from_json(cls, data, command_class=Command.from_json):
        """Create a class instance from a JSON object."""
        return cls(
            default=command_class(data.get('default', {})),
            iterations=list(map(command_class, data['iterations'])))

    def __init__(self, default, iterations):
        self.default = default
        self.iterations = iterations

    def __iter__(self):
        """Return a merged version of each iteration."""
        for iteration in self.iterations:
            yield Command.merge(iteration, self.default)

    def run(self, dry_run=False, verbose=False):
        """Run every merged iteration.

        - Dry run flag stops the iteration from being run.
        - Verbose flag announces each iteration.
        """
        for iteration in self:
            if verbose:
                iteration.announce()
            if not dry_run:
                iteration.run()


def load(path):
    """Shortcut for ``Configuration.load``."""
    return Configuration.load(path)
