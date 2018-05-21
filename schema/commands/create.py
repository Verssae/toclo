from .base import Base

class Create(Base):
    """Create Schedule.db"""

    def run(self):

        table_create_sql = """create table if not exists todo (
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        finished integer);"""

        self.cur.execute(table_create_sql)
        self.conn.commit()




