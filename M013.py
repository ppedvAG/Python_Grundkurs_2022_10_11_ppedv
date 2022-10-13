# Fehlerbehandlung

def doStuff(test):
	print(test)

# doStuff()  # Zu wenige Parameter (Syntax Error in PyCharm)

def rec():
	rec()

# rec()  # RecursionError, da die Funktion sich selber aufruft

# int(input("Gib eine Zahl ein: "))  # ValueError, falls der Benutzer keine Zahl eingibt

try:
	zahl = int(input("Gib eine Zahl ein: "))  # Hier kann ein ValueError auftreten wenn der User keine Zahl eingibt
	print(5 / zahl)  # Hier kann ein ZeroDivisionError auftreten wenn der User keine Zahl eingibt
except ValueError as e:
	print(e)  # Fehlermeldung ausgeben mit print(e) -> einfach Exception printen
	print("Das ist keine Zahl")
	# Aller möglicher Code hier möglich
	# Wird nur ausgeführt wenn der entsprechende Fehler auftritt
except ZeroDivisionError as e:  # e ist hier wieder frei belegbar
	print(e)
	print("Die Zahl darf nicht 0 sein")
except Exception as e:  # Exception wird nur betreten, wenn ein anderer Fehler als die in den except Statements gelisteten auftritt
	print(e)
	print("Ein anderer Fehler ist aufgetreten")
# except:
# 	print("Ein Exit-Error ist aufgetreten")  # except ohne Exception fängt ALLE Exceptions, kann kein e definieren
else:  # Else Block auch bei try-except möglich, wird ausgeführt wenn keine Exception aufgetreten ist
	print("Keine Fehler")
finally:  # Finally Block wird immer ausgeführt, auch wenn Fehler aufgetreten sind
	print("try-except fertig")

print("Code danach")

# Eigene Exception definieren
class CoffeeError(Exception):
	status = ""

	def printStatus(self):
		print(self.status)

	def __init__(self, message, status):  # Exception Konstruktor mit message über super() ansprechen
		super().__init__(message)
		self.status = status

coffee = 0

# if coffee < 1:
# 	raise CoffeeError  # Einen Fehler verursachen -> Programmabsturz


try:
	if coffee < 1:
		raise CoffeeError("Wir haben keinen Kaffee mehr", "Kaffee=0")  # Eigene Exception werfen
	else:
		raise ValueError  # Systemeigene Exception werfen
except CoffeeError as e:
	print(e)  # Wir haben keinen Kaffee mehr
	e.printStatus()  # Status ausgeben den ich oben beim raise definiert habe