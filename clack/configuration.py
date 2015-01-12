import subprocess

import json
import jsonschema

import clack.utils


with open(clack.utils.local_path('schema.json')) as f:
    SCHEMA = json.load(f)


class Command(object):
    @classmethod
    def from_json(cls, json):
        json.setdefault('command', None)
        json.setdefault('options', {})
        json.setdefault('arguments', [])
        return cls(**json)

    @classmethod
    def merge_default(cls, *values, default=None):
        """Returns the first "truthy" value from a series, or a default."""
        for value in values:
            if value:
                return value
        return default

    @classmethod
    def merge_options(cls, *options):
        """Merges a series of dictionaries, earlier values take precedence."""
        result = {}
        for d in options:
            for k, v in d.items():
                result.setdefault(k, v)
        return result

    @classmethod
    def merge(cls, a, b):
        """
        Returns a new Command instance merging the given Commands.

        The first ``Command`` passed to this function takes precedence.
        Attributes are merged based on the first "truthy" value, with the
        exception of options which are merged as a dictionary.
        """
        return cls(
            command=cls.merge_default(a.command, b.command),
            options=cls.merge_options(a.options, b.options),
            arguments=cls.merge_default(a.arguments, b.arguments, default=[]),
            description=cls.merge_default(a.description, b.description))

    def __init__(self, command, options, arguments, description=None):
        self.command = command
        self.options = options
        self.arguments = arguments
        self.description = description

    def __str__(self):
        return ' '.join(self.args)

    def __repr__(self):
        return '<{}: {!r}>'.format(self.__class__.__name__, self.args)

    @property
    def args(self):
        arguments = [self.command]
        for k, v in self.options.items():
            arguments.append(k)
            arguments.append(v)
        for a in self.arguments:
            arguments.append(a)
        return arguments

    def announce(self):
        if self.description is not None:
            print("#", self.description)
        print("$", self)

    def run(self):
        assert self.command is not None, "No command is set!"
        subprocess.check_call(self.args)


class Configuration(object):
    @classmethod
    def load(cls, path, schema=SCHEMA):
        with open(path, 'r') as f:
            data = json.load(f)
        jsonschema.validate(data, schema)
        return cls.from_json(data)

    @classmethod
    def from_json(cls, json, command_class=Command.from_json):
        return cls(
            default=command_class(json['default']),
            iterations=list(map(command_class, json['iterations'])))

    def __init__(self, default, iterations):
        self.default = default
        self.iterations = iterations

    def __iter__(self):
        for iteration in self.iterations:
            yield Command.merge(iteration, self.default)

    def run(self, dry_run=False, verbose=False):
        for iteration in self:
            if verbose:
                iteration.announce()
            if not dry_run:
                iteration.run()


def load(path):
    return Configuration.load(path)
