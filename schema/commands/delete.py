import sqlite3
import getpass
from .base import Base

class Delete(Base):
    def run(self):
        username = getpass.getuser()
        
        conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
        cur = conn.cursor()
        id = self.options['<delid>']
        sql = "DELETE FROM todo WHERE id=?"
        cur.execute(sql,(id,))
        conn.commit()