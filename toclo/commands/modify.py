from .base import Base

class Modify(Base):
    def run(self):
        if self.check_input(1):
            for i in range(4):
                if not self.check_ignore(i):
                    self.update_todo(i)
        else:
            print("Now allowed input data: ")
            print("You have to write due date such as 2018-05-05")
            print("or x if you don't want to set due date")

        self.show(None, 0)