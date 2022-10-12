# Funktionen

# Ein Code-Block der nur ausgeführt wird wenn wir ihn aufrufen
# Beispiele: len(...), list(...), string.split(...)
# print(Parameter1, Parameter2, ...)

# Wir können auch eigene Funktionen definieren
# Funktionen sind für Wiederverwendbarkeit zu benutzen
# Syntax:
# def <Name>(Optional: <Par1>, <Par2>, ...):
#	Code
# <Name>(<Par1>, <Par2>, ...)

def hallo():  # Funktion anlegen
	print("Hallo")


hallo()  # Funktion benutzen
hallo()


# Funktion mit Parameter
def halloName(name):  # Funktion mit Parameter
	print(f"Hallo {name}")


halloName("Lukas")
halloName(359)
halloName(True)
halloName({1, 2, 3})  # Alle möglichen Parameter möglich


def Addiere(x, y):
	return x + y  # Wert zurückgeben


ergebnis = Addiere(3, 4)  # Ergebnis aus der Funktion in eine Variable schreiben
print(ergebnis)


def AddiereFix(x: int, y: int):  # mit :<Typ> bei einzelnen Parametern einen Typ empfehlen
	return x + y


print(AddiereFix(3, 4))
print(AddiereFix("x", "y") * 4)  # Diese Eingabe funktioniert trotzdem
print(AddiereFix(4.2, 6.2))  # Auch mit floats funktioniert diese Funktion


def AddiereFixerReturn(x: int, y: int) -> int:  # Hier angeben mit -> <Typ> was für ein Wert heraus kommt
	return x + y


print(AddiereFixerReturn(5, 2) * 2)


# Default Werte
# Bei einem Parameter angeben was der Standardwert ist, und muss dann beim Aufruf diesen nicht übergeben
def Subtrahiere(x: int, y: int, z=0):  # optionaler Parameter z=0
	return x - y - z


Subtrahiere(3, 4)  # der Standardwert wird verwendet (0)
Subtrahiere(3, 4, 5)  # hier z=5

# Die Reihenfolge von Parametern kann verändert werden
Subtrahiere(y=5, x=1)  # besonders nützlich bei Funktionen mit 10+ Parametern wenn ich nur bestimmte Parameter befüllen möchte


def GenerierePerson(vn="", nn="", alter=0, addresse="", gender=""):
	print()  # Code ausführen


GenerierePerson(vn="Lukas", alter=24)  # Nur bestimmte Parameter setzen bei Funktionen


# * Parameter
# Gibt die Möglichkeit, beliebig viele Parameter zu übergeben
def sumNumbers(*numbers):  # Tuple mit allen Parametern
	x = 0
	for num in numbers:
		x += num
	return x


print(sumNumbers())
print(sumNumbers(3, 5, 2, 6))  # beliebig viele Parameter
print(sumNumbers(3, 5, 7, 1, 5, 87, 34, 7, 9))

# Unpacking Operator
intList = [2, 34, 6, 2, 4]
# print(sumNumbers(intList)) Geht nicht, da wir sonst ein Tupel von Listen haben
print(sumNumbers(*intList))  # mit * vor der Collection kann man diese Unpacken in ihre Einzelteile

intTuple = (32, 435, 7456, 1)
print(sumNumbers(*intTuple))  # Funktioniert auch mit Tupel und Set

print(sumNumbers(*range(1, 100)))  # Besonders praktisch bei Range


def spell(*word):
	for c in word:
		print(c)


spell("test")
spell(*"test")  # Unpacking Operator funktioniert auch bei Strings

(a, b, *c, d) = (1, 2, 3, 4, 5, 6)  # Jede Variable wird mit einem Feld gematcht, der Rest kommt in c
print(a)
print(b)
print(c)
print(d)


def halloGuests(**guests):
	for key in guests:  # Äquivalent zu guests.keys()
		print(guests[key])


testDict = { "Name1": "Das", "Name2": "ist", "Name3": "ein", "Name4": "Test" }

halloGuests(**testDict)  # Unpacken mit ** bei einem Dictionary


def printDict(**dictionary):
	for key, value in dictionary.items():  # in der Schleife auf Key und Value gleichzeitig greifen über Items
		print(f"{key}: {value}")


printDict(**testDict)  # Hier auch wieder Unpacken


def mixed(value1, *test, value2=123, **dictionary):
	print(value1)
	print(*test)
	print(value2)
	print(**dictionary)


mixed(2, "Text", 3, 4, 5, True)  # alles wird in *test gefüllt
mixed(3, 3, 2, "Test", **testDict, value1=321, value2=123)  # bis "Test" in *test, dann **testDict, dann optionale Parameter


def multiply(z1, z2, /, z3, z4):  # alle Argumente vor dem / müssen in der korrekten Reihenfolge angegeben werden
	print(z3 + z4)
	return z1 * z2


multiply(4, 2, z4=8, z3=9)  # die ersten zwei Argumente müssen in der korrekten Reihenfolge angegeben werden

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Paramter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Bonus: Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12












