
import pyodbc

class DBConnection:
    def __init__(self):
        self.conn=pyodbc.connect(conn_str)
        self.cursor=self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()