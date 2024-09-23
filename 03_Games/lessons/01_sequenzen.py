# Listen-Literal mit 3 Elementen
l = [3, "Hello", 5.0]
print(l)

# Zugriff auf das erste Element der Liste
l = [3, "Hello", 5.0]
print(f"Das erste Element der Liste ist {l[0]}")

# Ändern des zweiten Elements der Liste
l = [3, "Hello", 5.0]
l[1] = "Hallo"
print(f"Das zweite Element der Liste ist jetzt {l[1]}")

# Iteration über die Elemente einer Liste
liste = [3, "Hello", 5.0]
for element in liste:
    print(element)

# Iteration über ein Intervall
for zahl in range(3):
    print(zahl)

# Typen von Listen und Intervallen
print(type([3, "Hello", 5.0]))
print(type(range(3)))

# Iteration über die Zeichen eines Strings
for c in "Hallo":
    print(c)

# Konvertierung eines Strings in eine Liste
print(list("Hallo"))

# Tupel-Literal mit 3 Elementen, Zugriff, Iteration
tupel = (3, "Hello", 5.0)
print(tupel[2])
for element in tupel:
    print(element)

