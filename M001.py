# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht, also muss vor jeder Zeile das # Zeichen gesetzt werden

# Wie werden Variablen definiert?
# name = Wert

# Alle Variablen sind dynamisch, d.h. ihre Datentypen können sich ändern
# In Python gibt es keine Konstanten, jede Variable kann geändert werden

# Datentypen

# Einfache Datentypen

# Integer
# Ganze Zahl, egal ob positiv oder negativ
# Es gibt kein Integer Limit -> beliebig große Integer

zahl = 5  # x ist eine Variable

grosseZahl = 32859723579824658246598264592645923659426395862349562344356394856  # Beliebig große Zahl in Integer möglich

# Float
# Kommazahlen, immer mit . statt mit ,

kommazahl = 25.72

# String
# Textfolge, wird mit "" oder mit '' definiert

meinText = "Ein Text"
meinText2 = 'Ein Text'

# Boolean
# Wahr/Falsch Wert, True oder False möglich

wahr = True
falsch = False

# Methoden des Strings
# Methoden sind Funktionen, die zu einem Objekt gehören

text = "Max Mustermann"

# string.count("Ausdruck")
# Gibt an, wie oft ein Text in dem angegebenen String vorkommt
# Ist Case-Sensitive

text.count('n')

# Exkurs: print("")
# Schreibt den angegeben Parameter in die Konsole

print(text.count('n'))  # 2

print(text.count('m'))  # 1

# string.lower()
# Gibt einen neuen String zurück, der komplett kleingeschrieben ist
# Verändert nicht den originalen Wert
print(text.lower())
print(text)
text = text.lower()
print(text)

# string.upper()
# Gibt einen neuen String zurück der komplett aus GROßBUCHSTABEN besteht
# Verändert nicht den originalen Wert
print(text.upper())

# Methoden kann man verketten
print(text.lower().count('m'))  # 3

# string.islower() & string.isupper()
# Gibt einen Boolean zurück, der aussagt ob der gesamte String groß oder klein ist
print(text.islower())  # true (Zuweisung von vorhin, Zeile 62)
print(text.isupper())  # false

# Wir können mit einem Index einzelne Zeichen des Strings angreifen
# Der Index beginnt bei 0 und endet bei der Länge des Strings - 1
# Benutzung: string[Index]
print(text[0])  # m
print(text[3])  # Leerzeichen

print(text[0].isupper())  # False

# len(Variable)
# Gibt die Länge der Variable an
# Funktioniert nur bei Variablen mit Index (string, Listentypen)
print(len(text))  # 14

# print(text[len(text)])  # Versuche an die Stelle 14 zu greifen -> Fehler
print(text[len(text) - 1])  # n
print(text[len(text) - 1].islower())  # True

# Von rechts in einen String/Liste greifen
print(text[-1])  # Von rechts String angreifen (n)
print(text[-4])  # m

# Gibt einen Teil von einem String aus (Range Operator)
# Fängt bei 0 an bis zum 5ten Zeichen (max m)
# Nimmt eine Stelle weniger als ein normaler Index
print(text[0:5])  # Mittleren Teil eines Strings/Liste nehmen
print(text[0:5].islower())  # True
print(text[1:5])  # 1 bis 4
print(text[5])  # u

# string.isalpha()
# Prüft ob ein String nur aus Buchstaben besteht und gibt True oder False zurück
print(text.isalpha())  # False (Leerzeichen ist ein Sonderzeichen)

# string.isnumeric()
# Prüft ob ein String nur aus Zahlen besteht
print(text.isnumeric())  # False

# string.isalnum()
# Prüft ob ein String nur aus Zahlen und Buchstaben besteht
print(text.isalnum())  # False (Leerzeichen ist ein Sonderzeichen)

# complex
# Komplexe Zahlen
# j steht für den imaginären Teil

comp = 5 + 12j

# Arithmetische Operatoren in Python
# +, -, *, /
# % Modulo: Gibt den Rest einer Divison zurück
# ** Potenzierung
# // Ganzzahldivision, schneidet die Kommazahlen ab

x = 9
y = 4

print(x + y)  # 13 (keine Änderung der Variable x, nur das Ergebnis der Berechnung wird ausgegeben)

x = x + y  # Weise auf x das Ergebnis von x + y zu
x += y  # Selbiges wie oben nur kürzer

x %= y  # 1 Rest wird in x geschrieben
x **= y  # 6561 wird in x geschrieben
x //= y  # 1640.25 -> 1640 wird in x geschrieben

# Strings Multiplizieren
text *= 5
print(text)

# Strings aneinanderhängen
text += "Ein weiterer Text"
print(text)


# Übung1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable

# Übung2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist

# Übung3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein

# Übung4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus