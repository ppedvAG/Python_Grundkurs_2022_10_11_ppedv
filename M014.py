# Unittesting

# Teile meines Programms auf Fehler testen
# Erwartetes Verhalten im Test festlegen und dann den Code laufen lassen
# Schauen was passiert, über Konsolenausgabe sehen wir ob der Test erfolgreich war oder nicht

import unittest
from unittest import TestCase
from M014b import Rechner

class TestClass(TestCase):
	# Arrange, Act, Assert
	def testeAddiere(self):  # Testmethode definieren
		# Arrange
		r = Rechner(3, 4)
		expected = 7

		# Act
		result = r.add()

		# Assert
		self.assertEqual(result, expected)

	def testeSubtrahiere(self):
		r = Rechner(4, 9)
		expected = -5

		result = r.sub()

		self.assertEqual(result, expected, "Der Test ist falsch gelaufen")  # Fehler hier absichtlich erzeugen, Fehlermeldung als dritten Parameter

if __name__ == '__main__':  # Sollte immer im File sein um Tests zu aktivieren
	unittest.main()