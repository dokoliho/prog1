import random

COINS = 100000

def main():
    random.seed()
    blue = 0
    red = 0
    for _ in range(COINS):
        if is_thrown_coin_inside_circle():
            red += 1
        else:
            blue += 1
    print(f'Blau: {blue}, Rot: {red}, Pi: {4 * red / COINS:.4f}')

def is_thrown_coin_inside_circle():
    x = random.random()
    y = random.random()
    return x ** 2 + y ** 2 < 1

main()