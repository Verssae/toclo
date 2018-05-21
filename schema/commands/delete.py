import sqlite3
from .base import Base

class Delete(Base):
    def run(self):
        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()
        id = self.options['<delid>']
        sql = "DELETE FROM todo WHERE id=?"
        cur.execute(sql,(id,))
        conn.commit()