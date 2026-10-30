# Ausgabe von Geldbeträgen in einer speziellen Formatierung
def main():
    for money in [100123345, 100123305, 5]:
        print(format_money_string(money))


# Funktion zur Formatierung von Geldbeträgen
def format_money_string(total_cents):
    total_euros = total_cents // 100
    cents = total_cents % 100
    total_thousands = total_euros // 1000
    euros = total_euros % 1000
    millions = total_thousands // 1000
    thousands = total_thousands % 1000
    if millions > 0:
        return f'{millions}.{thousands:03}.{euros:03},{cents:02}'
    elif thousands > 0:
        return f'{thousands}.{euros:03},{cents:02}'
    else:
        return f'{euros},{cents:02}'


# Start des Programms
main()
