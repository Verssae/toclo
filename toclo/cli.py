"""
┌────────────────────┐
│toclo: the todo List│
└────────────────────┘

Usage:
    toclo -h | --help                             
    toclo --version                             
    toclo add <what> <due> [<ctgr>]             
    toclo ls [<ctgr> <done>]                    
    toclo modify <id> <what> <due> <ctgr> <v>   
    toclo delete (<id> | <all>)                 
    toclo complete <id>                         

Options:
    -h --help                       Show this screen
    --version                       Show version

Examples:
    toclo add "Study Hard" todo 2018-05-16 study
    toclo ls
    toclo modify 1 "Study not hard" - - -
    toclo complete 1
    toclo delete 1

Help:
    '-' : don't change
    <due>: 'YYYY-MM-DD' | [0~7] | 'x'(no due date)
    https://github.com/Verssae/toclo
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import toclo.commands
    options = docopt(__doc__, version=VERSION)
    

    for (k, v) in options.items():
        if hasattr(toclo.commands, k) and v:
            module = getattr(toclo.commands, k)
            toclo.commands = getmembers(module, isclass)
            command = [command[1] for command in toclo.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()