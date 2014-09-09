import clack
import click


@click.command
def main():
    clack.call('ssh borntyping.io')


if __name__ == '__main__':
    main()
