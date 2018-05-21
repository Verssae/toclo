from .base import Base

class Delete(Base):
    def run(self):
        id = self.options['<delid>']
        sql = "DELETE FROM todo WHERE id=?"
        self.cur.execute(sql,(id,))
        self.conn.commit()