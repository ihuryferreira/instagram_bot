import sqlite3

class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'insta.db'
        try:
            conexao = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao


    def createTableCliente(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS Cliente')

        sql = """CREATE TABLE IF NOT EXISTS Cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login VARCHAR (70) NOT NULL
                    senha VARCHAR (70) NOT NULL);"""

        cursor.execute(sql)
        conexao.commit()

    def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        self.createTableCliente(conexao,cursor)