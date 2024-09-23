# Ausgabe von Geldbeträgen in einer speziellen Formatierung
def main():
    for money in [100123345, 100123305, 5]:
        print(format_money_string(money))


# Funktion zur Formatierung von Geldbeträgen
def format_money_string(cents):
    euros = cents // 100
    cents = cents % 100
    thousands = euros // 1000
    euros = euros % 1000
    millions = thousands // 1000
    thousands = thousands % 1000
    if millions > 0:
        return f'{millions}.{thousands:03}.{euros:03},{cents:02}'
    elif thousands > 0:
        return f'{thousands}.{euros:03},{cents:02}'
    else:
        return f'{euros},{cents:02}'


# Start des Programms
main()
