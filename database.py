import sqlite3


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



