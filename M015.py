# Datenbankverbindung

# Hier verwenden wir sqlite3

import sqlite3 as sql  # Alias auf sql damit ich nicht immer sqlite3 schreiben muss

# Verbindung öffnen mit sql.connect(Name)
connection = sql.connect("Test.db")

# cursor: Verbindungsstück zwischen Datenbank und Code
cursor = connection.cursor()

# Mit dem Cursor können wir Befehle an die Datenbank senden
cursor.execute("create table if not exists test(id integer primary key, name text)")

id = input("Gib deine ID ein: ")
name = input("Gib deinen Namen ein: ")
# User nach den Werten fragen die in die Datenbank geschrieben werden

cursor.execute(f"insert into test(id, name) values ({id}, '{name}')")

# Sichergehen das Transaktionen ausgeführt werden
connection.commit()  # commit() befindet sich auf der Connection statt auf dem Cursor

# Daten aus dem Cursor entnehmen
# Mit fetchone(), fetchmany(Anzahl), fetchall() Daten entnehmen
cursor.execute("select * from test")  # Mit select Daten in Cursor schreiben
print(cursor.fetchall())

connection.close()  # Danach die Verbindung schließen

try:  # Fehler abwenden (falls zwei Programme gleichzeitig auf die DB zugreifen wollen, etc.)
	with sql.connect("Test.db") as conn:  # Der ganze obere Code mit dem with Statement
		cursor = connection.cursor()
		cursor.execute("create table if not exists test(id integer primary key, name text)")
		id = input("Gib deine ID ein: ")
		name = input("Gib deinen Namen ein: ")
		cursor.execute(f"insert into test(id, name) values ({id}, '{name}')")
		connection.commit()
		cursor.execute("select * from test")
		print(cursor.fetchall())
except sql.Error as err:
	print(err)