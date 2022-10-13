# Decorators
# Sind Funktionen, die das Verhalten von anderen Funktionen anpassen
# Werden mit @<Name> hinzugefügt
import time


# Auch Objekte sind Funktionen
def test():
	pass

print(test)  # Function Objekt

testFunc = test  # Funktionen können auch auf Variablen zugewiesen werden
print(type(testFunc))  # <class 'function'>

# Mit Decorator eine Funktion auf eine andere Funktion anhängen
def testDecorator(func):
	def wrapper():
		print("Ich werde vor der Funktion ausgeführt")
		func()
		print("Ich werde nach der Funktion ausgeführt")

	return wrapper  # Hier kommt die Dekorierte Funktion heraus

def hello():
	print("Hello World")

decoratedHello = testDecorator(hello)  # Hier lasse ich hello dekorieren

decoratedHello()  # dekorierte Funktion ausführen

# Kurzform:

@testDecorator
def bye():
	print("Bye World")

bye()


# Decorator mit Parametern
def doTwice(func):
	def wrapper(*args, **kwargs):  # *args: normale Parameter, **kwargs: benannte Argumente
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper

@doTwice
def printAddiere(z1, z2):
	print(z1 + z2)


printAddiere(3, 4)
printAddiere(z1=3, z2=8)


# Decorator mit Return
def doTwiceReturn(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
	return wrapper

@doTwiceReturn
def add(z1, z2):
	print(f"{z1}+{z2}={z1+z2}")
	return z1 + z2

zahl = add(3, 9)


class Square:
	def __init__(self, a: int):
		self._seitenlaenge = a  # private Variable, ist in Python auch nur eine Empfehlung

	@property
	def seitenlaenge(self):
		print("Die Seitenlänge wurde angegriffen")
		return self._seitenlaenge

	@seitenlaenge.setter
	def seitenlaenge(self, neuerWert):
		if 0 < neuerWert < 100:
			self._seitenlaenge = neuerWert
		else:
			print("Neue Seitenlänge ist nicht gültig")


square = Square(20)
print(square.seitenlaenge)  # property
print(square._seitenlaenge)  # Geht trotzdem, da private auch nur eine Empfehlung
square.seitenlaenge = 300  # seitenlaenge.setter


# Decorator zum Messen der Ausführungszeit
def measureTime(func):
	def wrapper(*args, **kwargs):
		startTime = time.time()
		func(*args, **kwargs)
		endTime = time.time()
		print(f"{endTime - startTime}s vergangen")
	return wrapper

@measureTime
def sumNumbers(*args):
	return sum(args)

sumNumbers(*range(100000000))