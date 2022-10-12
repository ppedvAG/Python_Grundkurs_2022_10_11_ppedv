from M007 import countCase  # Hier explizit angeben welche Funktionen/Klassen importiert werden
import sys
import numpy
import math

countCase("Text")
# calcTax()

# Module-Searchpath
# 1. Im selben Ordner, wie das ausgeführte Skript
# 2. PYTHONPATH, Ordner in dem Python selbst installiert ist
# 3. Liste an Ordnern, die wir bei der Installation von Python zusätzlich konfiguriert haben
# Wenn nach Punkt3 nichts gefunden wird => ModuleNotFoundError

# sys Modul:
# Alle möglichen Information zu der Umgebung von Python
# z.B.: Version, Suchpfade für Module, ...

print(sys.path)  # sys.path: Alle Pfade vom Projekt anzeigen (Python Runtime, Code Files, ...)
print(sys.version)  # sys.version: Derzeitige Python Version anzeigen (hier 3.10.6)
# sys.exit(0)  # sys.exit(Code): Programm beenden


def main():  # Einstiegspunkt des Programms wenn es unten mit der if festgelegt wird
	print("Ich führe M007b aus")
	countCase("Test")
	math.floor(4.5)  # math Package für einfache Mathematik
	numpy.floor(4.5)  # numpy Package für komplexe Mathematik

# Wie installiere ich ein zusätzliches Modul?
# 1. Entweder per Terminal:
# pip install <Name>
# pip uninstall <Name>
# 2. Über Python Packages Tab unten links

if __name__ == "__main__":
	main()