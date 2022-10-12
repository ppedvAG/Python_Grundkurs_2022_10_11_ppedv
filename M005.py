# List-Comprehension
# Anhand einer Expression kann man eine Liste konstruieren
numbers = [number for number in range(0, 101)]  # Alle Ergebnisse der for-Schleife werden in die Liste geschrieben
print(numbers)

evenNumbers = [num for num in range(0, 101) if num % 2 == 0]  # if noch hinzufügen
print(evenNumbers)

print([num ** num for num in range(0, 11)])  # Zahl vor dem Einfügen in die Liste noch bearbeiten

print([num ** num for num in range(0, 11) if num ** num % 2 == 0])  # Ausdruck links noch mit if einschränken

# Ohne List-Comprehension
# testList = []
# for num in range(0, 11):
# 	if num ** num % 2 == 0:
# 		testList.append(num ** num)
# print(testList)

# List-Comprehension mit 2 Schleifen
print([f"{z1}x{z2}={z1*z2}" for z1 in range(1, 11) for z2 in range(1, 11)])  # Kleines 1x1 mit List-Comprehension

testList2 = ["even" if num % 2 == 0 else "odd" for num in range(1, 101)]  # Ternary Operator in List-Comp
print(testList2)

stringList = ["IcH", "bIN", "eiN", "TeXt"]
print([wort.upper() for wort in stringList])  # List-Comp mit String Liste

print([wort.upper() if wort[0].isupper() else wort.lower() for wort in stringList])

print([wort.title() if wort[0].isupper() else wort.lower() for wort in stringList])  # Liste Fehler beheben

print([wort for wort in stringList if "e" in wort])  # Alle Wörter finden mit einem "e" drinnen

print([wort for wort in stringList if "e" in wort.lower()])  # Alle Wörter finden mit einem "e" (Case-Insensitive) drinnen

umlaut = ["Wörter", "Für", "Änderung", "Wort"]
umlaut = [wort.lower() for wort in umlaut]
print([wort.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue") for wort in umlaut if "ä" in wort or "ö" in wort or "ü" in wort])  # Umlaute ersetzen

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden
print([num + 12 for num in range(1, 31) if num % 6 == 0])

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
text = "Ich bin ein Text"
print([b.upper() for b in text if b.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
print([wort[0] for wort in text.split(" ")])
print([wort[0] for wort in text.title() if wort.isupper()])

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
print([wort for wort in text.split(" ") if len(wort) <= 3])

# Match-Case
test = "Ein Text"

# Syntax:
# match <Variable>:
# 	case <Bedingung>:
#		Code
#	case <Bedingung>:
#		Code

match test:
	case "Ein Text":
		print("Text ist Ein Text")
	case "Zwei Text":
		print("Text ist Zwei Text")
	case _ if len(test) >= 5:  # Bedingung hinzufügen mit _ als Platzhalter
		print("Test ist länger als 5")
	case _:  # default Case
		print("Etwas anderes")

if test == "Ein Text":
	print()
elif test == "Zwei Text":
	print()
elif len(test) >= 5:
	print()
else:
	print()