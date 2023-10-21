# Ćwiczenie z submodułu 13.2

# Tworzenie połączenia 
# Tworzenie poleceania wykonawczego SQL

# Tworzenie Tabel zależnych:
# -Tabela "Organizer" z listą pozycji do zrobienia>>
# -Tabela "List_off_things_to_do" lista poszczególnych czynności do wykonania przypisanych do konkretnych pozycji z tabeli "Organizer" 

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

def execute_sql(conn, sql):
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

if __name__ == '__main__':

    create_organizer_sql = """
    -- organizer table
    CREATE TABLE IF NOT EXISTS organizer (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        start_date text,
        end_date text
    );
    """

    create_list_off_things_to_do_sql = """
    -- list off things to do table
    CREATE TABLE IF NOT EXISTS list_off_things_to_do ( 
        id integer PRIMARY KEY,
        projekt_id integer NOT NULL,
        nazwa VARCHAR(250) NOT NULL,
        opis TEXT,
        status VARCHAR(15) NOT NULL,
        start_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (projekt_id) REFERENCES organizer (id)
    );
    """
    
    db_file = "Cwiczenie13_2_database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_organizer_sql)
        execute_sql(conn, create_list_off_things_to_do_sql)
        conn.close()
