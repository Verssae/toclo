from .base import *

class Complete(Base):
    def run(self):
        sql = "UPDATE todo set finished=1 where id = {}".format(self.options['<id>'])
        self.cur.execute(sql)
        self.conn.commit()
        self.show()