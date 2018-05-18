import sqlite3

from .base import Base
from .show import *

class Modify(Base):
    def run(self):

        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()
        
        modify_id = input("Record id? ") if self.options['<id>'] == None else self.options['<id>']
        modify_what = input("Todo? ") if self.options['<mwhat>'] == None else self.options['<mwhat>']
        modify_due = input("Due Date? ") if self.options['<mdue>'] == None else self.options['<mdue>']
        modify_finished = input("Finished (1: yes, 0: no)?") if self.options['<v>'] == None else self.options['<v>']

        sql = "UPDATE TODO set what = '{}', due = '{}', finished = '{}' where id = '{}'".format(modify_what, modify_due, modify_finished, modify_id)
        cur.execute(sql)
        conn.commit()
        show()