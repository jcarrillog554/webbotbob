#!/usr/bin/python
import psycopg2
import sys

hostname = 'localhost'
username = 'jonathan'
password = '123'
database = 'WebBotBob'

try:
    myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    myConnection.close()
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'" \
              % (hostname, database, username, password, 5432)
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("No se pudo establecer conexion a la base de datos!\n ->%s" % (exceptionValue))

# print the connection string we will use to connect
print
"Conectado a la database\n ->%s" % (conn_string)





