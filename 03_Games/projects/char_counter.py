
char = input("Geben Sie einen Buchstaben ein: ").lower()
text = input("Geben Sie einen Text ein: ").lower()

counter = 0
for c in text:
    if c == char:
        counter += 1

print(f"Der Buchstabe {char} kommt {counter} mal im Text vor.")

