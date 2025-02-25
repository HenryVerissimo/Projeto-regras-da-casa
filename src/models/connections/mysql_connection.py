import mysql.connector
from mysql.connector import Error

from .interface_connection import InterfaceConnection

class MysqlConnection(InterfaceConnection):

    def __init__(self, host, port, user, password) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password
            )

            if self.connection.is_connected():
                print("Conexão bem sucedida ao banco de dados")

        except Error as e: print(f"Erro ao tentar conectar ao MySQL: {e}")
    
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados fechada.")

            
conexao = MysqlConnection("localhost", "3306", "teste", "")
conexao.connect()
