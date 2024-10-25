# Zahlenraten für zwei Spieler

def main():
    print('Willkommen beim Zahlenraten!')
    number = enter_number()
    count = find_number(number)
    print(f"Die Zahl {number} wurde nach {count} Versuchen erraten.")


# Eingabe der zu erratenden Zahl durch Spieler 1
def enter_number():
    number = int(input("Spieler(in) 1, geben Sie die zu erratende Zahl ein: "))
    for _ in range(100):
        print()
    return number

# Erraten der Zahl durch Spieler 2
def find_number(number):
    count = 0
    guess = -1
    while guess != number:
        guess = int(input("Spieler(in) 2, geben Sie Ihren Tipp ein: "))
        count += 1
        if guess < number:
            print("Die Zahl ist größer.")
        elif guess > number:
            print("Die Zahl ist kleiner.")
    print('Glückwunsch! Die Zahl wurde erraten.')
    return count


main()