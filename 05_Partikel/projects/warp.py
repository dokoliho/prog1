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
MAX_ACCELERATION = 4
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
    stars = []
    for i in range(STAR_COUNT):
        star = Particle(0,0)
        init_one_star(star)
        stars.append(star)


def init_one_star(star):
    star.position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    star.velocity = (star.position[0] - WIDTH // 2, star.position[1] - HEIGHT // 2)
    star.velocity = normalize(star.velocity)
    star.acceleration = (star.velocity[0] * random.randint(1, MAX_ACCELERATION),
                         star.velocity[1] * random.randint(1, MAX_ACCELERATION))
    star.brightness = random.randint(128, 255)
    star.radius = random.randint(1, MAX_RADIUS)
    surface = pygame.Surface((star.radius * 2, star.radius * 2))
    pygame.draw.circle(surface,
                       (star.brightness, star.brightness, star.brightness),
                       (star.radius, star.radius),
                       star.radius)
    star.set_surface(surface.convert_alpha())


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
    for star in stars:
        star.update()
        if star.position[0] < 0 or star.position[0] > WIDTH or star.position[1] < 0 or star.position[1] > HEIGHT:
            init_one_star(star)
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for star in stars:
        star.draw(screen)
    pygame.display.flip()


# Start des Programms
main()