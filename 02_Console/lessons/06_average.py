# Berechnen des Durchschnitts einer Liste von Zahlen

sum = 0.0
count = 0

while True:
    input_text = input("Geben Sie eine Zahl ein (0 bricht ab): ")
    number = float(input_text)
    if number == 0:
        break
    sum = sum + number
    count = count + 1

if count == 0:
    print("Keine Zahlen eingegeben")
else:
    print(f"Der Durchschnitt ist {sum / count:.3f}")
