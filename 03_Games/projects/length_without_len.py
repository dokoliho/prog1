def main():
    print("Dieses Programm zählt die Anzahl der Zeichen in einem Text.")
    user_input = input("Geben Sie einen Text ein: ")
    count = 0
    for c in user_input:
        count += 1
    print(f"Der Text ist {count} Zeichen lang.")

main()
