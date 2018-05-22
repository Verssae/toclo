from .base import Base

class Modify(Base):
    def run(self):
        try:
            self.cur.execute("select * from todo where 1")
        except:
            self.create_db()
        
        modify_id = self.options['<id>']
        modify_what = self.options['<mwhat>']
        modify_due = self.options['<mdue>']
        modify_finished = self.options['<v>']

        what_val = modify_what
        due_val = modify_due
        finished_val = modify_finished

        modify_what = self.what_check.match(modify_what)
        
        modify_due = self.due_check.match(modify_due)
        
        modify_finished = self.fin_check.match(modify_finished)
        
        if modify_what and modify_due and modify_finished:
            self.date_verify(due_val)
            modify_what = modify_what.group()

            modify_due = modify_due.group()
            
            modify_finished = modify_finished.group()
        else:
            print("Now allowed input data: ")
            # print("You can wirte todo title to 15 length") 일단 한글 문제 때문에 입력 글자 수는 보류
            print("You have to write due date such as 2018-05-05")
            print("or x if you don't want to set due date")
            exit()

        if what_val == "-":
            if due_val == "-":
                insql = "finished = {}".format(modify_finished) if finished_val != '-' else ""
            else:
                insql = "due = '{}'".format(modify_due)
                insql += ", finished = {}".format(modify_finished) if finished_val != '-' else ""
        else:
            if due_val == "-":
                insql = "what = '{}'".format(modify_what)
                insql += ", finished = {}".format(modify_finished) if finished_val != '-' else ""
            else:
                insql = "what = '{}', due = '{}'".format(modify_what, modify_due)
                insql += ", finished = {}".format(modify_finished) if finished_val != '-' else ""
        
        sql = "UPDATE TODO set {} where id = {}".format(insql, modify_id)
        
        # sql = "UPDATE TODO set what = '{}', due = '{}', finished = '{}' where id = '{}'".format(modify_what, modify_due, modify_finished, modify_id)
        self.cur.execute(sql)
        self.conn.commit()
        self.show()