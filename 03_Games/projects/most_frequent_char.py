
def main():
    print("Dieses Programm zählt den am häufigsten vorkommenden Buchstaben in einem Text.")
    user_input = input("Geben Sie einen Text ein: ")
    highest_count, most_frequent_char = find_most_frequent_char(user_input)
    print(f"Der Buchstabe {most_frequent_char} kommt {highest_count} mal im Text vor.")


def find_most_frequent_char(user_input):
    most_frequent_char = ""
    highest_count = 0
    count = 0
    for c1 in user_input:
        for c2 in user_input:
            if c1 == c2:
                count += 1
        if count > highest_count:
            most_frequent_char = c1
            highest_count = count
        count = 0
    return highest_count, most_frequent_char

main()
