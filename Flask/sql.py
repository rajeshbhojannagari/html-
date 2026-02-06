import sqlite3 
con=sqlite3.connect('new_db.db')
cursor=con.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(50),
               email VARCHAR(50),
               course VARCHAR(50)
               )
               """)

con.commit()
con.close()
print(" data base sucessfully")