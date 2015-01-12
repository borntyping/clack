"""Command line entry point for clack."""

import click

import clack.configuration


@click.command()
@click.option('--dry-run', '-d', is_flag=True)
@click.option('--verbose', '-v', is_flag=True)
@click.argument(
    'path', type=click.Path(exists=True, dir_okay=False, readable=True))
def main(path, dry_run, verbose):
    """Load and run a configuration."""
    clack.configuration.load(path).run(dry_run=dry_run, verbose=verbose)
