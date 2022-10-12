# Kontrollstrukturen

# if-Anweisungen
# Werden in Kombination mit logischen Operatoren verwendet

# Vergleichsoperatoren
# <, >, <=, >= kleiner, größer, kleiner-gleich, größer-gleich | Ergebnis True oder Falsch
# ==, != gleich, ungleich

# if-Anweisung
# Überprüft eine Bedingung und führt den Code darin nur aus wenn diese Bedingung wahr ist
a = 4
b = 8

if a < b:  # Code unterhalb wird nur ausgeführt wenn die Bedingung True ist
	print("a kleiner b")  # Durch Tabs die Ebenen festlegen
	print("If Ende")  # Mehrere Teile Code in der selben If

print("Nach der If")  # Nach der If ohne Einrückung

# elif
# Wird ausgeführt wenn die if nicht True ist und hat eine zusätzliche Bedingung dabei
if a < b:
	print("a kleiner b")
elif a > b:  # wird nicht ausgeführt wenn die if ausgeführt wird
	print("a größer b")

# else
# Wird ausgeführt wenn keine if/elif ausgeführt wird
# Wenn irgendetwas anderes passiert
if a < b:
	print("a kleiner b")
elif a > b:
	print("a größer b")
else:
	print("a gleich b")

# Bei mehreren if-Statements hintereinander wird jedes geprüft
c = 100
if c > 100:
	print("c größer 100")
if c > 90:
	print("c größer 90")
if c > 80:  # Beide ifs werden betreten da sie nicht mit elif verknüpft wurden
	print("c größer 80")
else:  # Dieses else gehört zum if darüber
	print("c ist kleiner oder gleich 80")

# mit elif
if c > 100:
	print("c größer 100")
elif c > 90:
	print("c größer 90")
elif c > 80:
	print("c größer 80")
else:
	print("c ist kleiner oder gleich 80")

# elif wird nur betreten wenn die vorherige if oder elif false war

# Verschaltelte if-Blöcke
if a < b:
	print(a, "ist kleiner als", b)
	if a % 2 == 0:
		print("a ist gerade")  # Der Codeblock muss wieder eingerückt werden
	else:  # Anhand Einrückungen kann die else bei der inneren if oder der äußeren if angehängt werden
		print("a ist ungerade")

# Logische Operatoren
# and: Zwei Bedingungen verknüpfen, ist nur True wenn beide Bedingungen True sind
# or: Zwei Bedingungen verknüpfen, ist nur True wenn eine der beiden Bedingungen True sind
# not: Bedingung invertieren
# is: Sind Zwei Objekte identisch? Schaut auf Speicheradressen
# in: Ist ein Element in einer Liste enthalten?

c = 10
if a < b and a > c or not b == c:
	print("a ist kleiner als b und a ist größer als c")

liste = [1, 2, 3, 4]
if 3 in liste:
	print("Liste enthält 3")
else:
	print("Liste enthält keine 3")

# Ternary Operator
# Ermöglicht Verkürzung von If/Elses

if a < b:
	print("a kleiner b")
elif a > b:  # wird nicht ausgeführt wenn die if ausgeführt wird
	print("a größer b")
print("a kleiner b") if a < b else print("a größer oder gleich b")  # Mit Ternary

if a < b:
	print("a kleiner b")
elif a > b:
	print("a größer b")
else:
	print("a gleich b")
print("a kleiner b") if a < b else print("a gleich b") if a == b else print("a größer b")  # Mit Ternary