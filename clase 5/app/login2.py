from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login2 = Blueprint('login2', __name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'unida',
    'password': 'unida123',
    'database': 'jaguarete',
    'port': 3306
}

# Función para verificar credenciales
def verificar_credenciales(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None

    try:
        print("Verificar login")

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        query = "SELECT username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))

        result = cursor.fetchone()

        if result:
            usuario = result['username']
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'

        cursor.close()
        connection.close()

    except Error as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, usuario, accion

# Ruta del login2
@login2.route('/login2', methods=['POST'])
def login_endpoint():
    data = request.json
    user = data.get('user')
    password = data.get('password')

    codRes, menRes, usuario, accion = verificar_credenciales(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': usuario,
        'accion': accion
    }

    return jsonify(salida)
 