def main():
    char = input("Geben Sie einen Buchstaben ein: ")
    text = input("Geben Sie einen Text ein: ")
    counter = count_char(text, char)
    print(f"Der Buchstabe {char} kommt {counter} mal im Text vor.")


def count_char(text, char):
    counter = 0
    for c in text.lower():
        if c == char.lower():
            counter += 1
    return counter


main()
