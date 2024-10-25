# Rechenmaschine

def main():
    while True:
        repeat = input("Soll noch eine Addition durchgeführt werden? (j/n): ")
        if repeat == 'n':
            break
        zahl1 = float(input("Erste Zahl: "))
        zahl2 = float(input("Zweite Zahl: "))
        print(f"Die Summe beträgt {zahl1 + zahl2}")

main()
