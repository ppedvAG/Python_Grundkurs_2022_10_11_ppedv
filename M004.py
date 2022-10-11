# Schleifen

# for Schleife
# Verhält sich wie foreach in anderen Sprachen
# Wird verwendet um über eine Collection zu iterieren (List, Tuple, String, ...)
# Syntax:
# for <Variablenname> in <Liste>

liste = ['Ich', 'bin', 'eine', 'Liste']

for wort in liste:
	print(wort)
	print("Ein Wort wurde geschrieben")  # Zwei Zeilen Code ausführen pro Schleifendurchlauf

# for-Schleife mit Zähler
for i in range(0, 10):  # Eine Schleife die von 0 bis 9 geht
	print(i)

text = "Ein Text"
for zeichen in text:  # Mit for-Schleife über String gehen
	print(zeichen)

# break und continue
# break: Die Schleife beenden und mit dem Code danach weitermachen
# continue: Zum Schleifenkopf zurückspringen
for i in range(0, 10):
	print(i)
	if i == 5:
		break  # Hier die Schleife abbrechen

print("Test")

for i in range(0, 10):
	if i == 5:
		continue  # Code danach wird nicht ausgeführt, wir springen zum Schleifenkopf zurück
	print(i)

# else am Ende einer Schleife
# Code wird am Ende der Schleife ausgeführt, wenn kein break verwendet wurde
for i in range(0, 10):
	print(i)
	if i == 5:
		break  # Würde else verhindern
else:
	print("Schleife fertig")

# fstring, formatted String
# Code in einen String schreiben
# Syntax:
# f'Text1 {<Code>} Text2'
a = 5
fstring = f'Die Zahl ist {a}'  # Code im String einbauen
print(fstring)

for i in range(0, 10):
	# print("Die Zahl ist " + i.__str__())
	# print("Die Quadrierte Zahl ist " + (i * i).__str__())
	# print(i.__str__() + "^2=" + (i*i).__str__())
	print(f"Die Zahl ist {i}")
	print(f"Die Quadrierte Zahl ist {i*i}")
	print(f"{i}^2={i*i}")

betrag = 300
for jahr in range(0, 10):
	betrag *= 1.1
	print(f"{jahr}: {betrag}€")

# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz
for i in range(0, 100):
	if i == 0:
		print(i)
	elif i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 100 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden
for i in range(1, 200):
	if i.__str__()[-2:] in ["11", "12", "13"]:
		print(f"{i}: {i}th")
	elif i % 10 == 1:
		print(f"{i}: {i}st")
	elif i % 10 == 2:
		print(f"{i}: {i}nd")
	elif i % 10 == 3:
		print(f"{i}: {i}rd")
	else:
		print(f"{i}: {i}th")

# While Schleife
# Läuft solange die Bedingung True ist
# Zähler sollte dabei sein (in den meisten Fällen)
i = 0
while i < 10:
	print(i)
	i += 1  # Wichtig: Zähler erhöhen
else:
	print("Schleife fertig")

while True:  # Endlosschleife
	print("Text")
	i += 1
	if i == 500:
		break  # Break auch in While möglich, genauso wie continue

# Verschachtelte Schleifen
# Schleifen in Schleifen
# Wenn wir eine Liste von Listen haben, kann man mit dieser Schleife alle Unterlisten iterieren
verschachtelt = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for innen in verschachtelt:
	for zahl in innen:
		print(zahl)
		if zahl == 5:
			break  # break in einer verschachtelten Schleife springt in die äußere Schleife heraus