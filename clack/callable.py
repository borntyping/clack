import re
import subprocess


class Callable(object):
    @staticmethod
    def join(*args, sep=' '):
        return sep.join([x for x in args if x])

    def __init__(self, command, *, options={}, arguments=()):
        self.command = command
        self.options = []
        self.arguments = []

        self.add_options(options)
        self.add_arguments(arguments)

    def __str__(self):
        return self.join(
            self.command,
            self.join(*self.options),
            self.join(*self.arguments))

    def str_value(self, value):
        if re.search('\s', value):
            return '\'' + value.replace('\'', '\\\'') + '\''
        return value

    def add_option(self, option, value=None):
        if value:
            self.options.append('{}={}'.format(option, self.str_value(value)))
        else:
            self.options.append(self.str_value(value))

    def add_options(self, options):
        for option, value in options.items():
            self.add_option(option, value)

    def add_argument(self, argument):
        self.arguments.append(self.str_value(argument))

    def add_arguments(self, arguments):
        for argument in arguments:
            self.add_argument(argument)

    def run(self):
        print('$', str(self))
        subprocess.check_call(str(self))
        return self

    def wrap(self, command, seperator='--'):
        if seperator:
            self.add_argument(seperator)
        self.add_argument(str(command))
        return self
