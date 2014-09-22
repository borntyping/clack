import json
import functools

import click

import clack
import clack.callable


@click.command()
@click.option(
    '--dry-run', '-d', is_flag=True)
@click.argument(
    'path', type=click.Path(exists=True, dir_okay=False, readable=True))
def main(path, dry_run):
    with open(path, 'r') as f:
        data = json.load(f)

    prepare = functools.partial(clack.callable.Callable, dry_run=dry_run)

    environment = data.pop('environment', None)

    for iteration in data.pop('iterations'):
        command = prepare(**data)
        command.add_options(iteration.get('options', {}))
        command.add_arguments(iteration.get('arguments', []))

        if environment:
            env_command = prepare(environment['command'])
            env_seperator = environment.get('seperator', '--')
            env_command.wrap(command, seperator=env_seperator)
            return env_command.run()

        return command.run()
