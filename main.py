# Ćwiczenie z submodułu 13.2

# Tworzenie połączenia 
# Tworzenie poleceania wykonawczego SQL

# Tworzenie Tabel zależnych:
# -Tabela "Organizer" z listą pozycji do zrobienia>>
# -Tabela "List_off_things_to_do" lista poszczególnych czynności do wykonania przypisanych do konkretnych pozycji z tabeli "Organizer" 

# Dodanie pozycji do tabeli "Organizer"

# Dodanie pozycji do tabeli "List_off_things_to_do"


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

def add_project(conn, task):
    """
    Create a new task into the organizer table
    :param conn:
    :param task:
    :return: project id
    """
    sql = '''INSERT INTO organizer(nazwa, start_date, end_date)
             VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def add_dutie(conn, dutie):
    """
    Create a new dutie into the list_off_things_to_do table
    :param conn:
    :param dutie:
    :return: dutie id
    """
    sql = '''INSERT INTO list_off_things_to_do(projekt_id, nazwa, opis, status, start_date, end_date)
             VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, dutie)
    conn.commit()
    return cur.lastrowid

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

    task = (
        "Praca",
        "2023-10-23 07:00:00",
        "2023-10-23 15:00:00"
        )
    task2 = (
        "Nauka z Kodillą",
        "2023-10-23 21:00:00",
        "2023-10-23 24:00:00"
        )
    task3 = (
        "Dom",
        "2023-10-23 15:30:00",
        "2023-10-23 18:30:00"
        )
    task4 = (
        "Trening",
        "2023-10-23 18:30:00",
        "2023-10-23 20:00:00"
        )

    conn = create_connection("Cwiczenie13_2_database.db")
    pr_id = add_project(conn, task)
    pr_id = add_project(conn, task2)
    pr_id = add_project(conn, task3)
    pr_id = add_project(conn, task4)
    
    dutie = (
        1,
        "Próba szczelności gazociągu",
        "Zdjęcie próby szczelności z gazociągu w Dobrzyniewo Duże, ul. Jarzębinowa`",
        "started",
        "2023-10-23 09:00:00",
        "2023-10-23 09:30:00"
    )
    
    dutie1 = (
        1,
        "Wizyta w Urzędzie miasta Choroszcz",
        "Odbiór projektu tymczasowej organizacji ruchu",
        "started",
        "2023-10-23 10:30:00",
        "2023-10-23 10:45:00"
    )
    
    dutie2 = (
        1,
        "Dokumentacja odbiorowa",
        "Przygotowanie protokołów technicznych i końcowych na Dobrzyniewo Duże, ul. Jarzębinowa`",
        "started",
        "2023-10-23 12:00:00",
        "2023-10-23 15:00:00"
    )
    
    dutie3 = (
        2,
        "Moduł 13",
        "Skonczyć moduł 13",
        "started",
        "2023-10-23 20:00:00",
        "2023-10-23 21:30:00"
    )
    
    dutie4 = (
        2,
        "Moduł 14",
        "Zaliczyć moduł 14",
        "started",
        "2023-10-23 21:30:00",
        "2023-10-23 23:00:00"
    )
    
    dutie5 = (
        2,
        "Powtórka",
        "Powtórzyć materiał, który dzisiaj przysfoiłem",
        "started",
        "2023-10-23 23:00:00",
        "2023-10-23 24:00:00"
    )
    
    dutie6 = (
        3,
        "Obiad",
        "Przygotować smaczny obiad dla całej rodziny",
        "started",
        "2023-10-23 15:30:00",
        "2023-10-23 16:30:00"
    )
    
    dutie7 = (
        3,
        "Zabawa",
        "Wykorzystać czas na zabawę z Tymkiem",
        "started",
        "2023-10-23 16:30:00",
        "2023-10-23 18:30:00"
    )
    
    dutie8 = (
        4,
        "Pompki",
        "Wykonać tradycyjne pompki 4 x 25",
        "started",
        "2023-10-23 18:30:00",
        "2023-10-23 18:45:00"
    )
    
    dutie9 = (
        4,
        "Przysiady",
        "Wykonać tradycyjne przysiady 4 x 25",
        "started",
        "2023-10-23 18:45:00",
        "2023-10-23 19:00:00"
    )
    
    dutie10 = (
        4,
        "Wyciskanie",
        "Wykonać tradycyjne wyciskanie leżąc 4 x 25",
        "started",
        "2023-10-23 19:00:00",
        "2023-10-23 19:15:00"
    )
    
    dutie11 = (
        4,
        "Biceps",
        "Wykonać tradycyjne uginanie przedramion 4 x 25",
        "started",
        "2023-10-23 19:15:00",
        "2023-10-23 19:30:00"
    )
    
    dutie_id = add_dutie(conn, dutie)
    dutie_id = add_dutie(conn, dutie1)
    dutie_id = add_dutie(conn, dutie2)
    dutie_id = add_dutie(conn, dutie3)
    dutie_id = add_dutie(conn, dutie4)
    dutie_id = add_dutie(conn, dutie5)
    dutie_id = add_dutie(conn, dutie6)
    dutie_id = add_dutie(conn, dutie7)
    dutie_id = add_dutie(conn, dutie8)
    dutie_id = add_dutie(conn, dutie9)
    dutie_id = add_dutie(conn, dutie10)
    dutie_id = add_dutie(conn, dutie11)
    print(pr_id, dutie_id)
    conn.commit()