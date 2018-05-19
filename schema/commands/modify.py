import sqlite3

from .base import Base
from .show import *

class Modify(Base):
    def run(self):

        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()

        try:
            cur.execute("select * from todo where 1")
        except:
            print("Warning : you must create Schedule.db first\n")
            print("By using command 'schema -h' or 'schema --help' you can refer to doc")
            exit()
        
        modify_id = self.options['<id>']
        modify_what = self.options['<mwhat>']
        modify_due = self.options['<mdue>']
        modify_finished = self.options['<v>']
        
        insql = ""
        insql += "what = '{}'".format(modify_what) +"," if modify_what != '-' else " "
        insql += "due = '{}'".format(modify_due+",") if modify_due != '-' else " "
        
        insql += "finished = {}".format(modify_finished) if modify_finished != '-' else " "
        # print(insql)
        sql = "UPDATE TODO set {} where id = {}".format(insql, modify_id)
        print(sql)
        # sql = "UPDATE TODO set what = '{}', due = '{}', finished = '{}' where id = '{}'".format(modify_what, modify_due, modify_finished, modify_id)
        cur.execute(sql)
        conn.commit()
        show()