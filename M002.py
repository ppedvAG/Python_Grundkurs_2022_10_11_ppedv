# List
# Kann mehrere Werze in einer Variable speichern
# Hat einen Index wie String
# Ist veränderbar, es können neue Elemente hinzugefügt oder bestehende entfernt werden
# Duplikate sind erlaubt
# Verschiedene Datentypen sind erlaubt
# Empfehlung: Immer die gleichen Typen in der Liste haben/nicht mischen

liste = [1, 2, 3, 4, True, 'Ein Element']
print(liste)  # Liste kann einfach mit print ausgegeben werden

# Kann auch auf einzelne Werte zugreifen mittels Index
print(liste[4])  # True, da beginnend bei 0

# Kann auch mit einer Range angesprochen werden
print(liste[2:5])  # [3, 4, True], Obergrenze wieder exkludiert

# Range ohne Obergrenze gibt mir die restliche Liste vom Startpunkt
print(liste[2:])  # [3, 4, True, 'Ein Element']

# Range von der anderen Seite
print(liste[-3:-1])  # [True, 'Ein Element'], Untergrenze (-3) exkludiert

# list(Objekt)
text = "Ein Text"
stringListe = list(text)  # Wandelt den String in eine Liste um, jedes Zeichen wird ein Element in der Liste
print(stringListe)
print(stringListe[1])

# list.append(Element)
liste.append("Test")
print(liste)

liste.append(stringListe)  # Liste als letztes Element anhängen (verschachtelte Liste)
print(liste)

# Verschachtelte Liste ansprechen
print(liste[-1][0])  # -1: Die String Liste, 0: E

# Elemente entfernen

# list.pop(Index)
# Element an einer bestimmten Stelle entfernen
# Gibt das entfernte Element zurück (kann in eine Variable geschrieben werden)
entferntesElement = liste.pop(7)
print(entferntesElement)
print(liste)

# list.remove(Wert)
# Sucht nach dem Wert in der Liste und entfernt ihn
# Bei Bool aufpassen: 0 = False, 1 = True
liste.remove('Ein Element')
print(liste)
# liste.remove(10)  # Fehler, kann man in der Konsole nur ganz oben sehen

# list.clear()
# Entleert die Liste
# Keine Rückgabe
liste.clear()
print(liste)

# list.extend(Liste)
# Fügt die Elemente der angegebenen Liste an (als einzelne Elemente statt einer Liste)
liste.append(2)
liste.extend(stringListe)
print(liste)

# list.insert(Index, Wert)
# Fügt vor der angegebenen Stelle ein Element in die Liste ein
liste.insert(3, 'Hallo')
print(liste)

# list.count(Wert)
# Zähle die Vorkommnisse in der Liste von dem angegebenen Wert
liste.append(2)
print(liste)
print(liste.count(2))  # Kommt zwei mal vor

# list.index(Wert)
# Gibt den Index des ersten Vorkommens des Werts zurück
print(liste.index('E'))
print(liste.index('T', 2))  # Mit Startposition
print(liste.index('T', 2, 7))  # Mit Start- und Endposition

# list.reverse()
# Dreht die Liste um
liste.reverse()
print(liste)

# list.sort()
# Sortiert die Liste (standardmäßig Alphanumerisch, bei Objektlisten kann noch ein Key angegeben werden)
liste.remove(2)
liste.remove(2)
liste.sort()
print(liste)

# Tuple
# Verhalten sich ähnlich wie Listen
# Sind nicht veränderbar, keine neuen Elemente, bestehende Elemente können nicht verändert werden
# Duplikate sind erlaubt
# Datentypen können gemischt sein
# Index vorhanden
# Verschachtelbar

myTuple = (1, 2, 3, 'Test', False)
print(myTuple)

# tuple.count(Wert)
# Funktioniert wie bei der Liste
print(myTuple.count(2))

# tuple.index(Wert)
# Funktioniert wie bei der Liste
print(myTuple.index('Test'))

# Workaround um Werte im Tupel zu verändern
myTuple = list(myTuple)
myTuple[0] = 5
myTuple = tuple(myTuple)
print(myTuple)

tuple2 = (10, 11)
tuple3 = myTuple + tuple2
print(tuple3)

# Unpacking
# Löst iterierbare Objekt in ihre einzelnen Elemente auf und danach auf Variablen zuweisen
# Anzahl Inhalte der Liste müssen der Anzahl der Variablen entsprechen

unpacking = [1, 2, 3, 4]
(eins, zwei, drei, vier) = unpacking  # Einzelne Variablen
print(eins)
print(vier)

# Funktioniert auch bei String
unpackString = "Test"
(a, b, c, d) = unpackString
print(a)
print(b)


# Range
# Nichtveränderbare Sequenz von Integern
# Werden häufig in Listen umgewandelt

# Syntax:
# range(Startzahl) -> Sequenz aus <Startzahl> Integern von 0 bis <Startzahl>
# range(100) -> Sequenz aus 100 Integern 0-99
# Obergrenze exkludiert
# Untergrenze inkludiert
print(list(range(100)))  # 0 bis 99

# range(Startzahl, Endzahl) -> Sequenz aus <Endzahl> - <Startzahl> Integern von <Startzahl> von <Endzahl>
# range(50, 100) -> Sequenz von 50-99
print(list(range(50, 100)))

# range(Startzahl, Endzahl, Schrittgröße)
# range(0, 100, 5) -> Sequenz von 0-95
print(list(range(0, 100, 5)))  # Da Obergrenze exkludiert ist kommt die 100 nicht herein
print(list(range(0, 101, 5)))  # +1 um Obergrenze zu inkludieren

# Sets
# Funktioniert ähnlich wie Liste
# Kein Index -> keine Anpassungen bei vorhandenen Werten
# Keine Duplikate
# Verschiedene Datentypen, neue Werte können hinzugefügt werden, Werte können entfernt werden

mySet = {1, 2, 3, 4, 5}
print(mySet)

# set.add(Element)
# Fügt ein Element am Ende des Sets hinzu
mySet.add(6)
print(mySet)

# set.pop()
# Entfernt das erste Element aus dem Set
mySet.pop()
print(mySet)

# set.update(Liste)
# Fügt alle nicht vorhandenen Elemente hinzu
mySet.update(liste)
print(mySet)

# Liste mit Duplikaten einzigartig machen über Set
eindeutig = [1, 1, 2, 2, 2, 3, 4, 5, 5]
eindeutig = set(eindeutig)
eindeutig = list(eindeutig)
print(eindeutig)

# Dictionaries
# Liste von Key-Value Paaren
# Sind veränderbar
# Keine Key-Duplikate

myCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

print(myCar)  # Dictionary ausgeben lassen wie Liste
print(myCar["Year"])  # Dictionary ansprechen mit String Index (Name vom Key)

# Werte anpassen
myCar["Year"] = 2018
print(myCar)

# Wert anpassen mit der Update Methode
myCar.update({"Year": 2019, "Wheels": 4})
print(myCar)

# Weiteren Wert hinzufügen
myCar["KM"] = 50000
print(myCar)

# dictionary.setdefault("key", Wert)
# Füge den Eintrag hinzu wenn er nicht existiert
# Falls der Eintrag existiert wird der Wert zurückgegeben
print(myCar.setdefault("Wheels", 8))  # Gibt 4 zurück, da der Key bereits existiert
print(myCar.setdefault("FuelUsage", 7))  # Gibt 7 zurück, da der Key bereits existiert
print(myCar)

# dictionary.get(Key)
# Gibt den Wert zurück falls er existiert, sonst None
print(myCar.get("Wheels"))  # 4
print(myCar.get("Wheels2"))  # None, da kein Wert vorhanden

# print(myCar["Wheels2"])  # Fehler wenn Wert nicht existiert

# Inhalt vom Dictionary als Liste von Tupeln ausgeben
print(myCar.items())

# dictionary.keys() / dictionary.values()
# Gibt die Keys/Values als Liste aus
print(myCar.keys())
print(myCar.values())

# dictionary.popitem()
# Gibt das letzte Item als Tupel aus
print(myCar.popitem())

# dictionary.pop(Key)
# Entfernt ein Element aus dem Dictionary und gibt den Wert zurück
print(myCar.pop("Wheels"))
print(myCar)

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus
list4 = list1 + list2 + list3
print(list(set(list4)))

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden
print(list("Ein Text"))

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
print(list(range(0, 21, 2)))