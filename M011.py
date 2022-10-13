# Lambda

# Lambdas sind anonyme Funktion, also Funktionen die in einer Variable gespeichert werden können
# In anderen Sprachen mit =>
# In Python gibt es das lambda Keyword
# Eigenschaften
# - Sie haben keinen Namen
# - Sie haben beliebig viele Parameter
# - Braucht kein return
# - Darf nur eine Expression enthalten

# Aufbau: lambda <Parameter1>, <Parameter2>, ... : <Code>
add = lambda z1, z2: z1 + z2  # return ist hier integriert
printAdd = lambda z1, z2: print(z1 + z2)

print(add(1, 2))  # add gibt hier die Zahl zurück
printAdd(3, 2)  # printAdd gibt keinen Wert zurück (weil print(...))

def addF(z1, z2):  # Äquivalent zur add Lambda-Expression als Funktion
	return z1 + z2

# Lambdas können auch * Argumente enthalten
printZahlen = lambda *zahlen: print(zahlen)

printZahlen(2, 3, 4, 5, 6, 7)

# Lambdas dürfen keine Schleifen + break/continue enthalten und auch kein return

# Lambdas werden häufig als Parameter für Methoden verwendet
# filter(): filtert eine Liste
# map(): wandelt eine Liste in eine andere Form um

# Die filter() Funktion
# Syntax:
# filter(Funktion, Liste)
# Filtert die Liste anhand der übergeben Funktion
# Die Funktion muss bool zurückgeben
numberList = list(range(100))

# Liste filtern mit for
evenNumbersFor = []
for num in numberList:
	if num % 2 == 0:
		evenNumbersFor.append(num)

# Liste filtern mit List-Comprehension
evenNumbersComp = [num for num in numberList if num % 2 == 0]

# Liste filtern mit filter() + Lambda
# filter ohne Konvertierung gibt nur ein filter Objekt zurück
evenNumbersLambda = list(filter(lambda num: num % 2 == 0, numberList))
print(evenNumbersLambda)

# Ich kann auch statt Lambda-Expressions zu schreiben einfach eine extra Funktion definieren
def isEven(num):
	return num % 2 == 0

evenNumbersMethodPointer = list(filter(isEven, numberList))  # Methodenzeiger hier übergeben (nicht die Methode ausführen)
print(evenNumbersMethodPointer)

# Eigene Funktion mit einer Funktion als Zeiger in den Parametern
def filterList(liste, func):
	filtered = []
	for element in liste:
		if func(element):  # Funktion ausführen die am Funktionszeiger hängt
			filtered.append(element)
	print("filterList: ")
	return filtered

print(filterList(numberList, isEven))
print(filterList(numberList, lambda x: x % 2 == 0))

# Die map() Funktion
# Syntax:
# map(Funktion, Liste)
# Wandelt eine Liste in eine neue Form um
# Die Funktion darf keinen Wert zurückgeben
numberList = map(lambda num: num * 4, numberList)
print(numberList)  # Gibt auch wieder nur ein map Objekt zurück
numberList = list(numberList)
print(numberList)

# Mit der Map Funktion eine int Liste zu einer String Liste umwandeln
numberList = list(map(lambda num: f"Die Zahl ist: {num.__str__()}", numberList))
print(numberList)