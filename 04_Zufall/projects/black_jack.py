import random

COINS = 100
SUITS = ['Kreuz', 'Pik', 'Herz', 'Karo']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

def main():
    random.seed()
    coins = COINS
    while is_another_round_wanted(coins):
        coins -= 1
        init_game()
        if is_game_won():
            coins += 2


def is_another_round_wanted(coins):
    print(f"Sie besitzen {coins} Münzen.")
    if coins <= 0:
        return False
    repeat = input("Möchten Sie noch eine Runde spielen? (j/n)")
    return repeat.lower() == "j"


def init_game():
    global hand
    create_deck()
    hand = []
    for _ in range(2):
        pick_card()


def create_deck():
    global deck
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((suit, rank))


def pick_card():
    global deck, hand
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)
    return card


def is_game_won():
    global hand
    player_picks_cards()
    player_result = hand_value()
    if player_result > 21:
        print_hand()
        print ("Sie haben verloren.")
        return False
    hand = []
    computer_picks_cards(player_result)
    computer_result = hand_value()
    print_hand()
    if computer_result > 21:
        print ("Sie haben gewonnen.")
        return True
    print("Sie haben verloren.")
    return False


def player_picks_cards():
    print_hand()
    while hand_value() < 21:
        if offer_card() == False:
            break
        print_hand()


def print_hand():
    print("Karten:")
    for card in hand:
        print(f"  {card_as_string(card)}")


def card_as_string(card):
    return f"{card[0]} {card[1]}"


def offer_card():
    answer = input("Möchten Sie eine Karte ziehen? (j/n)")
    if answer.lower() == "j":
        card = pick_card()
        print(f"Sie ziehen {card_as_string(card)} ")
        return True
    return False


def computer_picks_cards(treshold):
    while hand_value() <= treshold:
        card = pick_card()
        print(f"Der Computer zieht {card_as_string(card)} ")

def hand_value():
    value = 0
    for card in hand:
        value += card_value(card)
    return value


def card_value(card):
    if card[1] == 'Bube' or card[1] == 'Dame' or card[1] == 'König':
        return 10
    if card[1] == 'Ass':
        return 11
    return int(card[1])


main()