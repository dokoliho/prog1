# Ausgabe von Geldbeträgen in einer speziellen Formatierung
def main():
    for money in [120, 90, 100, 102, 2]:
        print(format_money_string(money))


# Funktion zur Formatierung von Geldbeträgen
def format_money_string(money):
    euros = money // 100
    cents = money % 100
    return f'{euros},{cents:02}'


# Start des Programms
main()
