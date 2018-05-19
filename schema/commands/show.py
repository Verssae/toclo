import sqlite3
from .color import *

def show():
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    sql = "select * from todo where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    print_blue("┌─────┬─────────────────────────┬─────────────┬─────┐",'\n')
    print_blue('│')
    print_red("{:>5}".format("ID"))
    print_blue("│")
    print_cyan('{:>25}'.format("Todo"))
    print_blue("│")
    print_yellow('{:>13}'.format("Due"))
    print_blue("│")
    print_green('{:>5}'.format("Done"))
    print_blue("│",'\n')
    print_blue('├─────┼─────────────────────────┼─────────────┼─────┤','\n')

    for row in rows:
        print_blue("│")
        print_red('{:>5}'.format(str(row[0])))
        print_blue("│")
        print_cyan(preformat_cjk(row[1],25,'>'))
        print_blue("│")
        print_yellow('{:>13}'.format(row[2]))
        print_blue("│")
        print_green('{:^5}'.format(row[3]*"V"))
        print_blue("│",'\n')
    print_blue('└─────┴─────────────────────────┴─────────────┴─────┘','\n')
