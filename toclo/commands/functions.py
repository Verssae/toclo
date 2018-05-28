
# color reference : https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
import unicodedata
from colorama import init
from colorama import Fore, Back, Style
init()
 
def preformats(string, width, align='<', fill=' '):
    # refer from : https://sarc.io/index.php/development/810-python-print-format-padding
    # use it instead of '.format()'
    count = width - get_width(string)
    
    return {'>': lambda s: fill * count + s,
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * int(count / 2) + s + fill * int(count / 2 + count % 2) }[align](string)

def get_width(s):
    s = str(s)
    s_width = 0

    for c in s:
        c_ord = ord(c)
        if (
            (ord('A') <= c_ord <= ord('Z')) or
            (ord('a') <= c_ord <= ord('z')) or
            (ord('0') <= c_ord <= ord('9')) or
            (c in " !?()_-+=@#$%^&*\\/<>,.")
        ):
            s_width += 1
        elif (
            (ord('ㄱ') <= c_ord <= ord('ㅣ')) or
            (ord('가') <= c_ord <= ord('ퟻ'))
        ):
            s_width += 2
            
        else:
            return None
        

    return s_width    

def print_red(message, end = ''):
    print(Fore.RED + message,end=end)


def print_green(message, end = ''):
    print('\x1b[1;32m' + message + '\x1b[0m',end=end)


def print_yellow(message, end = ''):
    print('\x1b[1;33m' + message + '\x1b[0m',end=end)

def print_blue(message, end = ''):
    print('\x1b[1;34m' + message + '\x1b[0m',end=end)


def print_cyan(message, end = ''):
    print('\x1b[1;36m' + message + '\x1b[0m',end=end)