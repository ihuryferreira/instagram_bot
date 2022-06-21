import sqlite3
from sqlite3.dbapi2 import Error
from tkinter.constants import NONE
from conexao import Conexao

class InstaCrud:

    def cadastrar(self,login,senha):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Cliente (login,senha) VALUES (?,?)'
            cursor.execute(sql,(login,senha))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Clientes: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    
    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM Cliente').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

    def buscar(self,login):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
         
        
        try:
            resultset = cursor.execute('SELECT * FROM Cliente WHERE nome LIKE '%' ORDER BY login', (login,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")
            
        cursor.close()
        conexao.close()
        return resultset
    
    def consultar_detalhes(self, id):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM Cliente WHERE id = ?', (id,)).fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")


        cursor.close()
        conexao.close()
        return resultset


    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(id) FROM Cliente').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id,login,senha):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Cliente SET login = ?, senha = ? WHERE id = (?)'
            cursor.execute(sql,(login,senha, id))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de Cliente: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Cliente WHERE id = (?)'
            cursor.execute(sql,[id])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de Cliente: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False