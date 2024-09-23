# Gültigkeitsbereich von Variablen


# 1. Beispiel: Änderungen an lokalen Variablen beeinflussen globale Variablen nicht

a = 1   # Globale Variable

def f():
    a = 2  # Lokale Variable

f()
print(a)


# 2. Beispiel: Das Verdecken der globalen Variable durch eine lokale Variable
#              kann durch die Verwendung des Schlüsselworts 'global' verhindert werden

def f():
    global a
    a = 2

f()
print(a)


# 3. Beispiel: Eine globale Variable kann in einer Funktion erstellt werden

def f():
    global b
    b = 3

f()
print(b)

