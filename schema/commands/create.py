import sqlite3
import getpass
from .base import Base

class Create(Base):
    """Say hello, world!"""

    def run(self):
        username = getpass.getuser()
        
        conn = sqlite3.connect("/Users/"+username+"/Schedule.db")
        cur = conn.cursor()

        table_create_sql = """create table if not exists todo (
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        finished integer);"""

        cur.execute(table_create_sql)




