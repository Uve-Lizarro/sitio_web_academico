from psycopg2 import connect

def conectar():
    try:
        conexion = connect(
            host="localhost",
            database="db_academico",
            user="postgres",
            password="183464729"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False