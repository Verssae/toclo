from .base import Base

class Add(Base):
    def run(self):
        inputed_what = self.options['<what>']
        inputed_date = self.options['<due>']
        inputed_category = self.options['<category>']

        if inputed_what and inputed_date:

            date_verify = inputed_date

            inputed_what = self.what_check.match(inputed_what)
            inputed_date = self.due_check.match(inputed_date)

            if inputed_what and inputed_date:
                self.date_verify(date_verify)
                self.add_todo(inputed_what.group(), inputed_date.group(), inputed_category)
            else:
                print("Now allowed input data: ")
                # print("You can wirte todo title to 15 length") 일단 한글 문제 때문에 입력 글자 수는 보류
                print("You have to write due date such as 2018-05-05")
                print("or x if you don't want to set due date")
        self.show_all()
