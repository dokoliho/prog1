import math

GRAVITY = 9.8

def main():
    input_start_parameters()

    # Initialisierung
    speed = (v_null * math.cos(alpha), v_null * math.sin(alpha))
    acceleration = (0, -GRAVITY)
    position = (0, 0)
    time = 0

    # Simulation
    while position[1] >= 0:
        speed = (speed[0] + acceleration[0], speed[1] + acceleration[1])
        position = (position[0] + speed[0], position[1] + speed[1])
        print(f"Position: {position[0]:.2f}, {position[1]:.2f}")
        time += 1
    print(time, position[0])

    # Berechnung der exakten Werte
    flighttime = calculate_flighttime(alpha, v_null)
    print(f"Die exakte Flugzeit beträgt {flighttime:.2f} Sekunden.")
    distance = v_null * math.cos(alpha) * flighttime
    print(f"Die exakte Distanz beträgt {distance:.2f} Meter.")



def input_start_parameters():
    global alpha
    global v_null
    print("Simulation eines Kanonenschusses")
    alpha = float(input("Geben Sie den Abschusswinkel in Grad ein (0-90): "))
    v_null = float(input("Geben Sie die Abschussgeschwindigkeit in m/s ein: "))
    alpha = math.radians(alpha)


def calculate_flighttime(angle, velocity):
    return 2 * velocity * math.sin(angle) / GRAVITY

main()