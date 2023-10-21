# Ćwiczenie z submodułu 13.2

# Tworzenie połączenia 
# Tworzenie poleceania wykonawczego SQL

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to a SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def exevute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

