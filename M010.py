# Vererbung
# Klassen können eine Oberklasse haben und damit eine Vererbungshierarchie herstellen
# z.B.: Lebewesen ->
# Mensch, Hund, Katze
# Lebewesen ist die Oberklasse von Mensch, Hund und Katze und gibt ihre Variablen und Funktionen nach unten weiter
# z.B.: Lebewesen enthält name:string und bewegen(meter: int)
# Unterklassen haben die Variable und diese Funktion dann auch

class Lebewesen:
	def __init__(self, name: str):
		self.name = name
		print("Ein Lebewesen wurde erstellt")

	def __str__(self):
		"""
		Eine schöne Ausgabe des Objekts
		:return: Gibt eine Stringrepräsentation des Objekts aus
		"""
		return f"Mein Name ist {self.name}"

	def bewegen(self, meter: int):
		"""
		Eine Methode mit der sich ein Lebewesen bewegen kann
		:param meter: Die Distanz in Metern
		"""
		print(f"Mein {type(self)} hat sich um {meter}m nach vorne bewegt")  # type(self) passt sich an die Vererbung an

leb = Lebewesen("Max")
print(leb)
print(f"{leb.name}")
leb.bewegen(3)

# Mensch ist ein Lebewesen
# Für Vererbung müssen die Oberklassen in der Klammer stehen
# Mensch erbt name und bewegen() von Lebewesen
class Mensch(Lebewesen):
	"""
	Eine Mensch Implementation die von Lebewesen erbt
	"""
	def __init__(self, name, alter):
		# mit super() auf die Oberklasse zugreifen
		# hier den Konstruktor der Oberklasse auch ausführen (Verketten)
		# hier müssen alle Parameter übergeben werden
		super().__init__(name)
		self.alter = alter
		print("Ein Mensch wurde erstellt")

	def sprechen(self):  # Spezifizierung in der Mensch Klasse
		"""
		Eine Methode mit der der Mensch sprechen kann
		"""
		print("Der Mensch redet")

	def __str__(self):  # obere Methode überschreiben
		return super().__str__() + f" und ich bin {self.alter} alt."  # mit super().__str__() oberen Code ausführen


mensch = Mensch("Max", 33)  # __init__ kommt von oben
mensch.bewegen(3)  # bewegen() kommt auch von oben
print(mensch)  # Code von Lebewesen benutzen solange keine Überschreibung statt gefunden hat
mensch.sprechen()
# leb.sprechen() nicht möglich

# Kind Klasse bekommt alles von Lebewesen und Mensch gleichzeitig
class Kind(Mensch):
	pass  # pass: Platzhalter, hat keine Funktion, kann verwendet werden um leere Klassen/Funktionen zu machen

kind = Kind("Max", 12)
kind.bewegen(3)  # Methode von Lebewesen
kind.sprechen()  # Methode von Mensch

# docstring
# Wird geschrieben mit """ """
# Enthält Beschreibungen zu der derzeitigen Funktion/Klasse
# Mit :param oder :return können Parameter und der Rückgabewert beschrieben werden

# Übung:
# Erstelle eine Klasse Fahrzeug
# Sie soll über die Props:
# Motorstatus: bool
# maximale Geschwindigkeit: int
# derzeitige Geschwindigkeit: int
# Sie soll die __str__ Methode implementieren
# Sie soll eine beschleunigungs Methode implementieren, diese akzeptiert einen Parameter, die neue Geschwindigkeit
# Wenn die neue Geschwindigkeit <= maximale Geschwindigkeit ist, soll die derzeitige Geschwindigkeit angepasst werden

class Fahrzeug:
	def __init__(self, motorstatus, maxV, aktV):
		self.motorstatus = motorstatus
		self.maxV = maxV
		self.aktV = aktV

	def __str__(self):
		return f"Das Fahrzeug hat eine Maximalgeschwindigkeit von {self.maxV}, es fährt gerade ({self.motorstatus}) und fährt {self.aktV}km/h."

	def beschleunige(self, v: int):
		if self.motorstatus:
			if self.aktV + v > self.maxV:
				print("Zu hoch")
			else:
				self.aktV += v

fzg = Fahrzeug(True, 300, 0)
fzg.beschleunige(200)
print(fzg.__str__())