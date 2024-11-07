import pygame
import random
import math
from particle import Particle

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 200
SIZE = (WIDTH, HEIGHT)
FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAX_RADIUS = 3
MAX_ACCELERATION = 8
STAR_COUNT = 50


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    random.seed()
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    init_clock()
    init_stars()
    pygame.display.set_caption("Warp")
    return screen


# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Nahrung
def init_stars():
    global stars
    stars = [new_star() for _ in range(STAR_COUNT)]


def new_star():
    star = Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Der Stern bewegt sich weg von der Mitte des Bildschirms
    star.velocity = (star.position[0] - WIDTH // 2, star.position[1] - HEIGHT // 2)
    star.velocity = normalize(star.velocity)

    # Der Stern erhält eine zufällige Beschleunigung in die Richtung seiner Bewegung
    star.acceleration = (star.velocity[0] * random.randint(1, MAX_ACCELERATION),
                         star.velocity[1] * random.randint(1, MAX_ACCELERATION))

    # Der Stern erhält eine zufällige Helligkeit und Größe
    brightness = random.randint(128, 255)
    radius = random.randint(1, MAX_RADIUS)

    # Generierung der Oberfläche des Sterns
    surface = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surface,
                       (brightness, brightness, brightness),
                       (radius, radius),
                       radius)
    star.set_surface(surface.convert_alpha())
    return star


# Der Vektor wird auf die Länge 1 normiert
def normalize(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return (vector[0] / length, vector[1] / length)


# Game-Loop
def game_loop(screen):
    while True:
        if event_handling() == False:
            break
        if update_game() == False:
            break
        draw_game(screen)
        clock.tick(FPS)


# Beenden von Pygame
def exit_game():
    pygame.quit()


# Behandlung der Events
def event_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Aktualisierung des Spiels
def update_game():
    global stars
    new_stars = []
    for star in stars:
        star.apply_force((star.acceleration[0], star.acceleration[1]))
        star.update()
        if star.position[0] < 0 or star.position[0] > WIDTH:
            new_stars.append(new_star())
        elif star.position[1] < 0 or star.position[1] > HEIGHT:
            new_stars.append(new_star())
        else:
            new_stars.append(star)
    stars = new_stars
    return True



# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for star in stars:
        star.draw(screen)
    pygame.display.flip()


# Start des Programms
if __name__ == "__main__":
    main()