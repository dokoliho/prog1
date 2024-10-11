import random

suits = ["Kreuz", "Pik", "Herz", "Karo"]
ranks = ["7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f"{suit} {rank}")

random.seed()
random.shuffle(deck)

print(deck)