# Module in Python
# Sind Libraries, die uns zusätzliche Funktionalität anbieten die wir einbinden können
# Enthalten meistens nur Code der sich mit einem Thema befasst
# Müssen importiert werden und manchmal installiert werden

# Wie importiere ich Module?
# Syntax:
# import <Modulname>
# from <Modulname> import <Namen der Funktionen> (as <Alias>) (* um alles aus einem Modul zu importieren)

# import turtle -> bindet keine Funktionen direkt ein
# from turtle import *  # Funktionen in mein Modul einbinden
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# Die Variable __name__ enthält den Namen einer Python Datei
# Falls die Datei direkt ausgeführt wurde, ist der Name immer __main__
# Falls die Datei importiert wird ist __name__ der tatsächliche Dateiname

print(__name__)


def countCase(text: str):
	lower, upper, special = 0, 0, 0
	for char in text:
		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		else:
			special += 1
	print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")


def calcTax(price):
	return price * 1.2


if __name__ == "__main__":
	print("Ich bin das Hauptskript")
	print(__name__)