# Klassen und Objekte

# Objekt
# Alles in Python ist ein Objekt
# Jedes Objekt hat einen Typ (int, str, list, set, ...)
# Jedes Objekt hat die Variablen und Funktionen die von der Klasse vorgegeben werden
i = 12  # x Variable mit 12 (int) Objekt
i.as_integer_ratio()  # Variable hat die Funktionen die in der Klasse definiert werden
print(type(i))  # <class 'int'>

# isinstance(Variable, Typ)
print(isinstance(i, int))  # true
print(isinstance(i, object))  # true, da int von object erbt

# Klasse
# Eine Klasse ist ein Bauplan, aus dem Objekte erstellt werden können
# In der Klasse wird vorgegeben, welche Variablen und Funktionen meine Objekte haben werden

# Instanz
# Erstelltes Objekt

# Wie erstelle ich eine Klasse?
# Mit dem class Keyword mit einem Namen

class Table:
	material = "Aluminium"  # Klassenvariable

	# __init__: Wird ausgeführt, wenn das Objekt erstellt wird
	def __init__(self, beine: int, flaeche: float):
		print("Ein Tisch wurde erstellt")
		self.beine = beine  # Eine Klassenvariable erstellen im Konstruktor
		self.flaeche = flaeche

	# self: Bezieht sich auf das Objekt selbst
	# Muss am Anfang jeder Funktion stehen in eigenen Klassen
	def move(self, x, y):
		print(f"Tisch wurde bewegt zu den Koordinaten {x}, {y}")

	def __str__(self):
		return f"Dieser Tisch hat {self.beine} Beine und eine Fläche von {self.flaeche}cm²."


tisch = Table(4, 300)  # Tisch erstellen
tisch.move(3, 5)  # move() Methode vom Tisch aufrufen
print(tisch.beine)  # Werte aus meinem Objekt entnehmen
print(tisch.flaeche)

print(type(tisch))  # <class '__main__.Table'>
print(isinstance(tisch, Table))  # true

# In Python können Instanzen neue Attribute (Properties) erhalten
# <Variablenname>.<Neuer Propertyname> = <Wert>
# Dynamic Properties sollten vermieden werden

tisch.bild = r"C:\..."
print(tisch.bild)

del tisch.bild  # del: Variable wegwerfen

print(tisch)  # Ohne __str__: <__main__.Table object at 0x000001EDF93DBFD0>
print(tisch)  # Mit __str__: Dieser Tisch hat 4 Beine und eine Fläche von 300cm².