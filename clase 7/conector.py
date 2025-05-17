import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(  # <- CORREGIDO 'connect'
            host='localhost',
            user='unida',
            password='unida123',
            database='jaguarete',
            port=3306
        )

        if conexion.is_connected():  # <- CORREGIDO 'is_connected'
            print("Conexión exitosa a la base de datos")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            resultado = cursor.fetchone()
            print("Base de datos actual:", resultado)

    except Error as e:
        print("Error al conectar a MySQL:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():  # <- CORREGIDO
            conexion.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    conectar_mysql()

    