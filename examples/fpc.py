import os.path
import site

site.addsitedir(os.path.abspath('.'))

import clack
import click


@click.command()
def main():
    defaults = {
        '--source': 'python',
        '--target': 'rpm',
        '--vendor': 'Sam Clements',
        '--epoch': '0'
    }

    packages = {
        'riemann-client': {
            '--version': '5.0.0',
            '--interation': '1'
        },
        'supermann': {
            '--version': '3.0.0',
            '--interation': '1'
        }
    }

    for package, package_options in packages.items():
        command = clack.prepare('fpm', arguments=[package])
        command.add_options(defaults)
        command.add_options(package_options)

        env_command = clack.prepare('scl', arguments=('enable', 'python27'))
        env_command.wrap(command, seperator='--')
        env_command.run()

if __name__ == '__main__':
    main()
