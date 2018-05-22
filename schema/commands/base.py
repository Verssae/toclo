"""The base command."""
import getpass
import sqlite3
import re
from .color import *

class Base(object):
    """A base command."""
    table_name = "todo"
    category_name = "categories"

    def __init__(self, options):
        self.options = options
        #create DB
        username = getpass.getuser() + "/Documents"
        self.conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
        self.cur = self.conn.cursor()
        self.create_todo_table()
        self.create_category_table()
        # self.what_check = re.compile("^-|([가-힣]|[a-zA-Z]|[0-9])*$")
        self.due_check = re.compile("^([0-9]{4}-[0-9]{2}-[0-9]{2})|x|-$")
        self.fin_check = re.compile("^0|1|-$")

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def check_input(self):
        "입력값이 올바른지 검사"
        pass
    
    def add_todo(self, what, due, category):
        if not self.check_category(category):
            self.add_category(category)
            print("New category is added: {}".format(category))
        sql = "insert into '{}' (what, due, category, finished) values ('{}', '{}', '{}', {})".format(
            self.table_name,
            what, due, category, 0
        )
        self.cur.execute(sql)
        self.conn.commit()
    
    def check_category(self, input_category):
        sql = "select * from '{}' where category='{}'".format(
            self.category_name,
            input_category
        )
        try:
            self.cur.excute(sql)
        except:
            return False
        return True

    
    def add_category(self, new_category):
        sql = "insert into '{}' (category) values ('{}')".format(
            self.category_name,
            new_category
        )
    
    def remove_row(self, table_name, id):
        sql = "DELETE FROM '{}' WHERE id={}".format(table_name, id)
        self.cur.execute(sql)
        self.conn.commit() 
    
    def get_max_column(self,columns):
        return max(map(get_width,columns))

    def show_all(self):
        self.cur.execute("select * from todo where 1")
        rows = self.cur.fetchall()
        id_max = 3 
        whats = ["Todo"]
        dues = ["Due"]
        categories = ["Category"]
        for row in rows:
            whats.append(row[1])
            dues.append(row[2])
            categories.append(row[3])
        what_max = self.get_max_column(whats)
        due_max = self.get_max_column(dues)
        category_max = self.get_max_column(categories)
        fin_max = 3
        
        print("┌",end="")
        print("─"* id_max,end="") 
        print("┬",end="")
        print("─"* what_max,end="") 
        print("┬",end="")
        print("─"* due_max,end="") 
        print("┬",end="")
        print("─"* category_max,end="") 
        print("┬",end="")
        print("─"* fin_max,end="") 
        print("┐")

        print('│',end="")
        print(preformats("ID",id_max,'^'),end="")
        print('│',end="")
        print(preformats("Todo",what_max,'^'),end="")
        print('│',end="")
        print(preformats("Due",due_max,'^'),end="")
        print('│',end="")
        print(preformats("Category",category_max,'^'),end="")
        print('│',end="")
        print(preformats("F",fin_max,'^'),end="")
        print('│')

        print("├",end="")
        print("─"* id_max,end="") 
        print("┼",end="")
        print("─"* what_max,end="") 
        print("┼",end="")
        print("─"* due_max,end="") 
        print("┼",end="")
        print("─"* category_max,end="") 
        print("┼",end="")
        print("─"* fin_max,end="") 
        print("┤")
        # print("└",end="")
        # print("┘")
        # print("┴",end="")

        for row in rows:

            print('│',end="")
            print(preformats(str(row[0]),id_max,'^'),end="")
            print('│',end="")
            print(preformats(row[1],what_max,'^'),end="")
            print('│',end="")
            print(preformats(row[2],due_max,'^'),end="")
            print('│',end="")
            print(preformats(row[3],category_max,'^'),end="")
            print('│',end="")
            print(preformats(str(row[4]),fin_max,'^'),end="")
            print('│')

        print("└",end="")
        print("─"* id_max,end="") 
        print("┴",end="")
        print("─"* what_max,end="") 
        print("┴",end="")
        print("─"* due_max,end="") 
        print("┴",end="")
        print("─"* category_max,end="") 
        print("┴",end="")
        print("─"* fin_max,end="") 
        print("┘")
    
    def delete(self):
        id = self.options['<delid>']
        self.remove_row(self.table_name,id)
        self.show_all()
    
    def create_todo_table(self):
        sql = """create table if not exists '{}' (
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        category text not null,
        finished integer);""".format(self.table_name)

        self.cur.execute(sql)
        self.conn.commit()
    
    def create_category_table(self):
        sql = """create table if not exists '{}' (
            id integer primary key autoincrement,
            category text not null
        );""".format(self.category_name)
        self.cur.execute(sql)
        self.conn.commit()