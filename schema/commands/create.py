import sqlite3
from .base import Base

class Create(Base):
    """Say hello, world!"""

    def run(self):
        conn = sqlite3.connect("Schedule.db")
        cur = conn.cursor()

        table_create_sql = """create table if not exists todo (
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        finished integer);"""

        cur.execute(table_create_sql)




