import sqlite3
import re
import getpass
from .base import Base
from .show import *

class Modify(Base):
    def run(self):
        username = getpass.getuser()
        
        conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
        cur = conn.cursor()
        p = re.compile("^([가-힣]|[a-zA-Z]|[0-9])*|-$")
        q = re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2})|x|-$")
        v = re.compile("^0|1|-$")

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
        modify_what = p.match(modify_what)
        modify_due = q.match(modify_due)
        modify_finished = v.match(modify_finished)
        if modify_what and modify_due and modify_finished:
            modify_what = modify_what.group()
            modify_due = modify_due.group()
            modify_finished = modify_finished.group()
        else:
            print("Now allowed input data: ")
            # print("You can wirte todo title to 15 length") 일단 한글 문제 때문에 입력 글자 수는 보류
            print("You have to write due date such as 2018-05-05")
            print("or x if you don't want to set due date")
            exit()

        if modify_what == "-":
            if modify_due == "-":
                insql = "finished = {}".format(modify_finished) if modify_finished != '-' else ""
            else:
                insql = "due = '{}'".format(modify_due)
                insql += ", finished = {}".format(modify_finished) if modify_finished != '-' else ""
        else:
            if modify_due == "-":
                insql = "what = '{}'".format(modify_what)
                insql += ", finished = {}".format(modify_finished) if modify_finished != '-' else ""
            else:
                insql = "what = '{}', due = '{}'".format(modify_what, modify_due)
                insql += ", finished = {}".format(modify_finished) if modify_finished != '-' else ""
        if insql == "":
            show()
            exit()
        sql = "UPDATE TODO set {} where id = {}".format(insql, modify_id)
        
        # sql = "UPDATE TODO set what = '{}', due = '{}', finished = '{}' where id = '{}'".format(modify_what, modify_due, modify_finished, modify_id)
        cur.execute(sql)
        conn.commit()
        show()