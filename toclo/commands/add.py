from .base import Base

class Add(Base):
    def run(self):
        if self.check_input(0):
            self.add_todo()
        else:
            print("Now allowed input data: ")
            print("You have to write due date such as 2018-05-05")
            print("or 0~7 if you set due date to today+number")
            print("or x if you don't want to set due date")
        self.show(None, 0)