def main():
    print("Dieses Programm zählt die Anzahl der Zeichen in einem Text.")
    text = input("Geben Sie einen Text ein: ")
    count = count_chars(text)
    print(f"Der Text ist {count} Zeichen lang.")


def count_chars(text):
    count = 0
    for _ in text:
        count += 1
    return count


main()
