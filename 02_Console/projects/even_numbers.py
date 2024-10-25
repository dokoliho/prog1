# Ermittlung, ob das Farbband gewechselt werden muss
# (immer an geraden Tagen)

def main():
    # Eingabe
    day = int(input('Welchen Kalendartag haben wir heute (1-31): '))

    # Berechnung
    if day % 2 == 0:
        print('Wechsel das Farbband!')
    else:
        print('Alles gut!')

main()
