import random

suits = ["Kreuz", "Pik", "Herz", "Karo"]
ranks = ["7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f"{suit} {rank}")

random.seed()
card = random.choice(deck)

print(card)
deck.remove(card)
print(deck)
print(len(deck))
