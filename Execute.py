from Flask import *
import psycopg2
import sys
from Conexion import *

def mostrarEstados(): #dice lo que el Webbot sabe hacer
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT definicion FROM Estados")
        salida = ""
        rows = cursor.fetchall()
        for row in rows:
            salida += row[0] + "\n"
        return salida

    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))

def aprender_BD(parametro):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        salida = ""
        param =  str(parametro)
        cursor.execute("SELECT simbolo FROM sign where significado = %s",[param])
        for row in cursor:
            salida += str(row[0])
        cursor.execute("insert into Estados (simbolo,definicion) values (%s,%s)", [salida, param])
        conn.commit()
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))

def consulta(parametro):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        salida = ""
        cursor.execute("SELECT simbolo FROM estados where simbolo = %s",[parametro])
        for row in cursor:
            salida += str(row[0])
        if salida != "":
            return "si"
        else:
            return "no"
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))


def deleteEstado(sim):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Estados WHERE simbolo = %s", (sim))
        conn.commit()
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))

def saveLogs(ip, date,time, number1,usuario):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("insert into Logs (ip,fecha,hora,numero1,usuario) values (%s,%s,%s,%s,%s)", [ip, date,time, number1,usuario])
        conn.commit()
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))

def saveInfo(nombre, hash, creadora, fecha):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(
        "insert into info (nombre,hash,creadora,fecha) values (%s,%s,%s,%s)",
        [nombre, hash, creadora, fecha])

        conn.commit()
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Problemas al guardar los datos!\n ->%s" % (exceptionValue))

