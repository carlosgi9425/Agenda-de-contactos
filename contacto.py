# CONTACTO
from conexion import *

# REGISTRAR
def registrar(nombre, apellidos, empresa, telefono, email, direccion):
    try: 
        con = conectar()
        cursor =con.cursor()
        sentencia_sql = ''' INSERT INTO contactos(
            nombre, apellidos, empresa, telefono, email, direccion) values 
            ( ?, ?, ?, ?, ?, ? ) '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion )
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return "Registro correcto"
    except sqlite3.Error as err:
        print("Ha ocurrido un error", err)
        
# CONSULTAR
def mostar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contactos '''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print("Ha courrido un error", err)
    return datos


# BUSCAR
def buscar(id):
    datos = []
    try: 
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contactos WHERE id = ? '''
        cursor.execute(sentencia_sql, (id))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print(" Ha ocurrido un error", err)
    return datos

# modificar
def modificar(id, nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        setencia_sql = '''  UPDATE contactos SET nombre=?, apellidos =?, empresa=?, telefono=?, email=?, direccion=? WHERE id=?'''
        datos = (nombre, apellidos, empresa, telefono, email, direccion, id)
        cursor.execute(setencia_sql, datos)
        con.commit()
        con.close()
        return "Se actualizo correctamente"
    except sqlite3.Error as err:
        print("Ha ocurrido un error", err)
        
        
#ELIMINAR
def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        setencia_sql = ''' DELETE FROM contactos WHERE id=?'''
        cursor.execute(setencia_sql, (id,))
        con.commit()
        con.close()
        return "Se elimino correctamente"
    except sqlite3.Error as err:
        print("Ha ocurrido un error", err)        