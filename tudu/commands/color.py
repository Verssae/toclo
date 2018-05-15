
# color reference : https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
import unicodedata
 
def preformat_cjk (string, width, align='<', fill=' '):
    # refer from : https://sarc.io/index.php/development/810-python-print-format-padding
    # use it instead of '.format()'
    count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in string))
    return {'>': lambda s: fill * count + s,
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2) + s + fill * (count / 2 + count % 2) }[align](string)
    
def print_red(message, end = ''):
    print('\x1b[1;31m' + message + '\x1b[0m',end=end)


def print_green(message, end = ''):
    print('\x1b[1;32m' + message + '\x1b[0m',end=end)


def print_yellow(message, end = ''):
    print('\x1b[1;33m' + message + '\x1b[0m',end=end)

def print_blue(message, end = ''):
    print('\x1b[1;34m' + message + '\x1b[0m',end=end)


def print_cyan(message, end = ''):
    print('\x1b[1;36m' + message + '\x1b[0m',end=end)