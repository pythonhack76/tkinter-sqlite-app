import sqlite3
import datetime 
import os


def check_db_exist():
    database = 'database.db'
    percorso = os.getcwd()
    lista = os.listdir(percorso)
    print("files nella directories is '", percorso, "' :")
    isExist = os.path.exists(database)
   
    if isExist == True:
        print(isExist)
    else:
        crea_database()
    #print(lista)
    # for x in os.listdir(): 
    #     list = []
    #     list.append(x)
    #     database_file = "database.db"
    #     isExist = os.path.exists(database_file)
    #     print(isExist)
      

def crea_database():
    try:
        conn = sqlite3.connect("database.db")

        cursor = conn.cursor() 
        print("database creato")

    except sqlite3.Error as error:
        print("abbiamo riscontrato un errore", error)
    finally:
        if conn:
            conn.close()
            print("connessione terminata")

    try:
        conn = sqlite3.connect('database.db')
        create_table_query = '''CREATE TABLE IF NOT EXISTS clienti(
                            id INTEGER PRIMARY KEY autoincrement NOT NULL,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            created_at datetime, 
                            totale REAL NOT NULL);'''

        cursor = conn.cursor() 
        print("connessione al database")
        cursor.execute(create_table_query)
        conn.commit()
        print("tabella creata")

        cursor.close() 
    except sqlite3.Error as error:
        print("abbiamo un errore durante la creazione della tabella", error)
    finally:
        if conn:
            conn.close() 
            print("la connessione è terminata")

#dati fake 
nome = 'pippo'
email = 'pippo@gmail.com'
totale = 1000
created_at = datetime.datetime.now()


#funzione per inserire nuovi items nella tabella 
def insert_into_db():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        print("connessione effettuata")

        conn_insert_query = '''INSERT INTO clienti (nome, email, created_at, totale) VALUES (:nome,:email, :created_at, :totale)'''

        count = cursor.execute(conn_insert_query)
        conn.commit()
        print("dati inseriti con successo", cursor.rowcount)
        cursor.close() 

    except sqlite3.Error as error:
        print("non abbiamo potuto inserire dati nella tabella")
        print(f'{nome} , {email} , {totale} , {created_at}')
    finally:
        if conn: 
            conn.close()
            print('la connessione al database è terminata con successo!')


check_db_exist() 

#insert_into_db() 

