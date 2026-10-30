START_ALTITUDE = 50000
START_VELOCITY = -1000
START_FUEL = 10000
ACCELERATION = -1.63
PUSH = 12
FUEL_CONSUMPTION = 100
THRESHOLD = -10


def main():
    altitude = START_ALTITUDE
    velocity = START_VELOCITY
    fuel = START_FUEL

    while altitude > 0:
        print_status(altitude, velocity, fuel)
        fire = ask_for_thrust()
        velocity += ACCELERATION
        if fire and fuel > 0:
            velocity += PUSH
            fuel -= FUEL_CONSUMPTION
        altitude += velocity

    print_result(velocity)


# Ausgabe des aktuellen Zustands
def print_status(altitude, velocity, fuel):
    print(f"Höhe: {altitude}, Geschwindigkeit: {velocity}, Treibstoff: {fuel}")


# Abfrage, ob die Bremsrakete gezündet werden soll
def ask_for_thrust():
    game_input = input("Bremsrakete zünden (J/N)?")
    return game_input.lower() == "j"


# Ausgabe des Ergebnisses
def print_result(velocity):
    if velocity < THRESHOLD:
        print("Crash")
    else:
        print("Landing")


main()
