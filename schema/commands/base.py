"""The base command."""
import getpass
import sqlite3
import re
from .color import *

class Base(object):
    """A base command."""

    def __init__(self, options):
        self.options = options

        username = getpass.getuser() + "/Documents"
        self.conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
        self.cur = self.conn.cursor()
        self.what_check = re.compile("^-|([가-힣]|[a-zA-Z]|[0-9])*$")
        self.due_check = re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2})|x|-$")
        self.fin_check = re.compile("^0|1|-$")

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def show(self):
        try:
            self.cur.execute("select * from todo where 1")
        except:
            self.create_db()
            self.cur.execute("select * from todo where 1")

        rows = self.cur.fetchall()

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
    
    def delete(self):
        id = self.options['<delid>']
        sql = "DELETE FROM todo WHERE id=?"
        self.cur.execute(sql,(id,))
        self.conn.commit()
    
    def create_db(self):
        table_create_sql = """create table if not exists todo (
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        finished integer);"""

        self.cur.execute(table_create_sql)
        self.conn.commit()