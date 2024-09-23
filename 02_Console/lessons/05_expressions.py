# Thema: Ausdrücke

# Ausführungsreihenfolge
print(3 * 4 - 8 // 2)
print(3 * (4 - 8) // 2)

# Operatoren bei unterschiedlichen Typen
print(4.0 + 2)
print (4 * 2.0)
print(4 / 2)

# Formatierte Ausgabe
print(f'Das Ergebnis ist {3+4}')

s = 'Haus'
z = 7
print(f'{s:10} ist ein Gebäude')
print(f'{z:010} ist eine Zahl')

euro = 20 / 3
print(f'Das kostet {euro:.2f} €.')


# Mehrere Ausdrücke in einem f-String
eingabe = 5
print(f'Das Quadrat von {eingabe} ist {eingabe*eingabe:.2f}')


print(f'{3+4} {3*4} {3-4} {3/4} {3//4} {3%4} {3**4}')