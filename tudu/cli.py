"""
┌───────────────────┐
│tudu: the Todo List│
└───────────────────┘

Usage:
    tudu -h | --help
    tudu --version
    tudu create
    tudu add [<what> <due>]
    tudu ls
    tudu modify [<id> <mwhat> <mdue> <v>]

Options:
    -h --help                       Show this screen
    --version                       Show version

Examples:
    tudu create
    tudu add Test todo 2018-05-16
    tudu ls
    tudu modify 1 Test tudu 2018-05-16 1

Help:
    https://github.com/Verssae/to_do_list_133
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import tudu.commands

    options = docopt(__doc__, version=VERSION)

    # 인자 처리하는 부분
    for (k, v) in options.items():
        if hasattr(tudu.commands, k) and v:
            module = getattr(tudu.commands, k)
            tudu.commands = getmembers(module, isclass)
            command = [command[1] for command in tudu.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()