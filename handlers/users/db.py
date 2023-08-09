from sqlite3 import Connection

class Database:
    def __init__(self, file):
        self.conn = Connection(file)
        self.c = self.conn.cursor()

    def create(self, tableName, values):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}({values})""")
        self.conn.commit()
    def insert(self, tableName, values):
        self.c.execute(f"""INSERT INTO {tableName} VALUES ({values}) """)
        self.conn.commit()
    def delete(self, TABLEnAME):
        self.c.execute(f"""DELETE FROM {TABLEnAME}""")
        self.conn.commit()

def main():
    DB = Database("data.db")
    DB.create("users", "id TEXT, name TEXT, menus TEXT, filesCount TEXT")
    DB.insert("users", """ "123", "Odilbek", "main", "0" """)
    DB.delete("users")
    DB.conn.close()
main()