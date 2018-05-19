import sqlite3
import re
from .base import Base

class Add(Base):
    def run(self):
        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()
        p = re.compile("^([가-힣]|[a-zA-Z]|[0-9])*$")
        q = re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2})|-$")

        try:
            cur.execute("select * from todo where 1")
        except:
            print("Warning : you must create Schedule.db first\n")
            print("By using command 'schema -h' or 'schema --help' you can refer to doc")
            exit()
        inputed_what = self.options['<what>']
        inputed_date = self.options['<due>']
        if inputed_what and inputed_date:
            inputed_what = p.match(inputed_what)
            inputed_date = q.match(inputed_date)
        
            if inputed_what and inputed_date:
                sql = "insert into todo (what, due, finished) values (?, ?, 0)"
                cur.execute(sql,(inputed_what.group(), inputed_date.group()))
                conn.commit()
            else:
                print("Now allowed input data: ")
                # print("You can wirte todo title to 15 length") 일단 한글 문제 때문에 입력 글자 수는 보류
                print("You have to write due date such as 2018-05-05")
                print("or - if you don't want to set due date")


        
            
        
