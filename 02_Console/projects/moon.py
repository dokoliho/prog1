START_ALTITUDE = 50000
START_VELOCITY = -1000
START_FUEL = 10000
ACCELERATION = -1.63
PUSH = 12
FUEL_CONSUMPTION = 100
TRESHOLD = -10

def main():
    altitude = START_ALTITUDE
    velocity = START_VELOCITY
    fuel = START_FUEL

    while altitude > 0:
        print(f"Höhe: {altitude}, Geschwindigkeit: {velocity}, Treibstoff: {fuel}")
        game_input = input("Bremsrakete zünden (J/N)?")
        velocity += ACCELERATION
        if (game_input == "J" or game_input == "j") and fuel > 0:
            velocity += PUSH
            fuel -= FUEL_CONSUMPTION
        altitude += velocity

    if velocity < TRESHOLD:
        print("Crash")
    else:
        print("Landing")


main()