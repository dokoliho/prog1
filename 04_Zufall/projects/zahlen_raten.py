import random

MAX_NUMBER = 100

def main():
    print('Willkommen beim Zahlenraten!')
    random.seed()
    number = pick_number()
    count = find_number(number)
    print(f"Die Zahl {number} wurde nach {count} Versuchen erraten.")


def pick_number():
    number = random.randint(1, MAX_NUMBER)
    print(f"Die zu erratende Zahl liegt zwischen 1 und {MAX_NUMBER}.")
    return number


def find_number(number):
    count = 0
    guess = -1
    while guess != number:
        guess = int(input("Geben Sie Ihren Tipp ein: "))
        count += 1
        if guess < number:
            print("Die Zahl ist größer.")
        elif guess > number:
            print("Die Zahl ist kleiner.")
    print('Glückwunsch! Die Zahl wurde erraten.')
    return count


main()