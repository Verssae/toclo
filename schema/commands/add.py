import sqlite3
from .base import Base

class Add(Base):
    def run(self):
        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()

        try:
            cur.execute("select * from todo where 1")
        except:
            print("Warning : you must create Schedule.db first\n")
            print("By using command 'schema -h' or 'schema --help' you can refer to doc")
            exit()

        inputed_what = self.options['<what>']
        inputed_due = self.options['<due>']

        if inputed_what == None:
            inputed_what = input("Todo? ")
        if inputed_due == None:
            inputed_due = input("Due Date? ")
            
        sql = "insert into todo (what, due, finished) values (?, ?, 0)"
        cur.execute(sql,(inputed_what, inputed_due))
        conn.commit()
