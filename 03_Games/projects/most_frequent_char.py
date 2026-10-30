
def main():
    print("Dieses Programm zählt den am häufigsten vorkommenden Buchstaben in einem Text.")
    text = input("Geben Sie einen Text ein: ")
    if text == "":
        print("Der Text ist leer.")
        return
    # Die Funktion liefert ein Tupel mit zwei Werten zurück
    result = find_most_frequent_char(text)
    # Das Tupel wird auf zwei einzelne Variablen aufgelöst (Unpacking)
    (highest_count, most_frequent_char) = result
    # Alternativ mit Indizes:
    # highest_count = result[0]
    # most_frequent_char = result[1]
    print(f"Der Buchstabe {most_frequent_char} kommt {highest_count} mal im Text vor.")


def find_most_frequent_char(text):
    most_frequent_char = ""
    highest_count = 0
    for c1 in text:
        count = 0
        for c2 in text:
            if c1 == c2:
                count += 1
        if count > highest_count:
            most_frequent_char = c1
            highest_count = count
    return (highest_count, most_frequent_char)


main()
