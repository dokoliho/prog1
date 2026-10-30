# Zahlenraten für zwei Spieler
MIN_NUMBER = 1
MAX_NUMBER = 100
EMPTY_LINES = 100


def main():
    print('Willkommen beim Zahlenraten!')
    number = enter_number()
    count = find_number(number)
    print(f"Die Zahl {number} wurde nach {count} Versuchen erraten.")


# Eingabe der zu erratenden Zahl durch Spieler 1
def enter_number():
    number = 0
    while number < MIN_NUMBER or number > MAX_NUMBER:
        number = int(input(f"Spieler(in) 1, geben Sie die zu erratende Zahl ({MIN_NUMBER}-{MAX_NUMBER}) ein: "))
    for _ in range(EMPTY_LINES):
        print()
    return number


# Erraten der Zahl durch Spieler 2
def find_number(number):
    count = 0
    while True:
        guess = int(input("Spieler(in) 2, geben Sie Ihren Tipp ein: "))
        count += 1
        if guess < number:
            print("Die Zahl ist größer.")
        elif guess > number:
            print("Die Zahl ist kleiner.")
        else:
            break
    print('Glückwunsch! Die Zahl wurde erraten.')
    return count


main()
