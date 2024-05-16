import pyodbc

class Dbconnection:
    def open(self):
        try:
            conn_str = PropertyUtil.get_property_string()
            self.conn = pyodbc.connect(conn_str)
            self.stmt = self.conn.cursor()
            print('Database connected..')
        except Exception as e:
            print(str(e) + '---Database Not Connected:--')

    def close(self):
        self.conn.close()
        print('Connection Closed:')


class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-0EUUQEO\\SQLEXPRESS"
        database_name = "SISDB"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
        return conn_str


obj = Dbconnection()
obj.open()
# Perform database operations here
obj.close()
