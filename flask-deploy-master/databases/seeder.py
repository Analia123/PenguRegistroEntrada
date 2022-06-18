import sqlite3 as sql

#CREO UNA RUTA ABSOLUTA A MI BASE DE DATOS
DB_PATH = "./datitos.db"

#CREAMOS BASE DE DATOS A UTILIZAR
def crearBD():
    conectar = sql.connect(DB_PATH)
    cursor = conectar.cursor()
    cursor.execute("""CREATE TABLE datitos (
        nombre text,
        apellido text,
        fecha date,
        hora time,
        numero text
    )""")
    cursor.execute("""CREATE TABLE marcaciones (
        fecha date,
        hora time,
        numero text
    )""")
    conectar.commit()
    conectar.close()

#DEFINIMOS UNA VARIABLE PARA AGREGAR DATOS CON TUPLES
def agregarval():
    conectar = sql.connect(DB_PATH)
    cursor = conectar.cursor()
    datos = [
        ("Steven", "Britez", "2019-06-23", '09:10:00', "AS1000")
    ]
    cursor.executemany("""INSERT INTO datitos VALUES (?, ?, ?, ?, ?)""", datos)
    datos2 = [
        ( "2019-06-23", '09:10:00', "AS1000")
    ] 
    cursor.executemany("""INSERT INTO marcaciones VALUES ( ?, ?, ?)""", datos2)
    conectar.commit()
    conectar.close()

if __name__ == "__main__":
    crearBD()
    agregarval()