import mysql.connector
from mysql.connector import Error

class DBConexion:
    def __init__(self) -> None:
        self.conexionGlobal = None
        try:
            # Establecer conexión con la base de datos
            self.conexionGlobal = mysql.connector.connect(
                host="localhost",       # Dirección del servidor de la base de datos
                user="isaac",           # Nombre de usuario
                password="roblox123",  # Contraseña del usuario
                database="abarrotes"  # Nombre de la base de datos
            )

            # Verificar si la conexión es exitosa
            if self.conexionGlobal.is_connected():
                print("Conexión exitosa a la base de datos")
                
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.conexionGlobal = None

    def obtener_cursor(self):
        if self.conexionGlobal:
            return self.conexionGlobal.cursor()
        else:
            print("No se puede obtener el cursor: conexión no establecida.")
            return None

    def cerrar_conexion(self):
        if self.conexionGlobal:
            self.conexionGlobal.close()
            print("Conexión cerrada.")