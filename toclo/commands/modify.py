from .base import Base

class Modify(Base):
    def run(self):
        if self.check_input(1):
            self.update_todo()
        else:
            print("Now allowed input data: ")
            print("You have to write due date such as 2018-05-05")
            print("or 0~7 if you set due date to today+number")
            print("or x if you don't want to set due date")
            print("or - if you don't want to change")

        self.show()