import sqlite3
import getpass
from .color import *

def show():
    username = getpass.getuser()
        
    conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
    cur = conn.cursor()
    
    try:
        cur.execute("select * from todo where 1")
    except:
        print("Warning : you must create Schedule.db first\n")
        print("By using command 'schema -h' or 'schema --help' you can refer to doc")
        exit()

    rows = cur.fetchall()

    print_blue("┌─────┬────────────────────────────┬─────────────┬─────┐",'\n')
    print_blue('│')
    print_red("{:>5}".format("ID"))
    print_blue("│")
    print_cyan('{:>28}'.format("Todo"))
    print_blue("│")
    print_yellow('{:>13}'.format("Due"))
    print_blue("│")
    print_green('{:>5}'.format("Done"))
    print_blue("│",'\n')
    print_blue('├─────┼────────────────────────────┼─────────────┼─────┤','\n')

    for row in rows:
        print_blue("│")
        print_red('{:>5}'.format(str(row[0])))
        print_blue("│")
        print_cyan(preformat_cjk(row[1],28,'>'))
        print_blue("│")
        print_yellow('{:>13}'.format(row[2]))
        print_blue("│")
        print_green('{:^5}'.format(row[3]*"V"))
        print_blue("│",'\n')
    print_blue('└─────┴────────────────────────────┴─────────────┴─────┘','\n')
