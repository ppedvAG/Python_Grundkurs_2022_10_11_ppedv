from os.path import exists
import json
# Input/Output

# Es gibt in Python mehrere Funktionen für Ein-/Ausgaben
# print(...)
# input(String)
# Wartet auf den Input des Benutzers und schreibt dann die Eingabe in eine Variable
# Programm bleibt stehen bis eine Eingabe passiert

# name = input("Gib deinen Namen ein: \n")  # Escape-Sequenzen: \n Zeilenumbruch, \t Tab
# print(f"Dein Name ist {name}")
#
# zahl = int(input("Gib eine Zahl ein: \n"))
# print(f"Deine gewählte Zahl mal Zwei ist {zahl * 2}")

# open(Path, Mode)
# Öffnet einen Stream zu einer Datei mit dem gewählten Modus
# w - Write, Overwrite
# a - Append
# r - Read
# x - Create
# r+ - Read/Write
# w+ - Read/Write, aber erstellt die Datei neu


# Funktion um ein neues File zu erstellen anhand eines Inputs des Benutzers
def createFile():
	fileName = input("Gib den Dateinamen ein: \n")
	if not exists(fileName):  # exists kommt von os.path, mit Alt + Eingabe importieren
		open(fileName, "x")
	else:
		print("File existiert bereits")


# createFile()


# Funktion um ein bestehendes File zu öffnen
def openFileWrite(fileName):
	return open(fileName, "a")  # Datei öffnen im Anhängemodus


file = openFileWrite("Test.txt")
file.write("Ein Text\n")  # Einen Text in die Datei
file.close()  # Das File wieder schließen, wenn es geöffnet bleibt können andere Prozesse nicht darauf zugreifen


def openFileRead(fileName):
	return open(fileName, "r")  # Datei öffnen im Lesemodus


readFile = openFileRead("Test.txt")
lines = readFile.readlines()  # Alle Zeilen einlesen
for line in lines:  # mit for-Schleife die ausgelesenen Zeilen iterieren
	print(line)


with openFileRead("Test.txt") as file:  # with-Block: wird automatisch geschlossen wenn der Block zu Ende ist
	for line in file.readlines():  # in der for-Schleife direkt auf readlines() zugreifen
		print(line)


pfad = "C:\\Users\\lk3"  # Um einen Backslash zu machen müssen Zwei Backslashes geschrieben werden
pfadR = r"C:\Users\lk3"  # r-String, Raw String: Interpretiert keine Escape-Sequenzen (kein \n, \t, \\)

# Übung:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden
def auswahl():
	choice = input("Gib w, r oder a ein: ")
	while True:  # Endlosschleife bis der User etwas korrektes eingibt
		# if choice == "w" or choice == "r" or choice == "a":
		if choice in ["w", "r", "a"]:  # in statt if/or
			break
		else:
			choice = input("Gib w, r oder a ein: ")
	print("Valide Eingabe, File wird geöffnet")
	return open("Test.txt", choice)

auswahl()