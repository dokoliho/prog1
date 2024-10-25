# Temperaturumrechnung

def main():
    f = float(input("Geben Sie die Temperatur in Fahrenheit ein: "))
    c = (f - 32) * 5 / 9

    print(f"Die Temperatur in Celsius beträgt {c:.1f}")

main()