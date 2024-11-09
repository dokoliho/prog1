import pygame
import random
from particle import Particle

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (100, 150, 200)

CIRCLE_RADIUS = 4
GRAVITY = (0, 0.1)
DROP_RATE = 2 # per second

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
    pygame.display.set_caption("Tap")
    init_clock()
    init_drops()
    return screen


# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Tropfen
def init_drops():
    global drops
    global new_drop_timer
    drops = []
    new_drop_timer = pygame.event.custom_type()
    pygame.time.set_timer(new_drop_timer, 1000 // DROP_RATE)


def add_drop():
    global drops
    drop_particle = Particle(WIDTH // 2, 0)
    surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2))
    surface.fill(WHITE)
    surface.set_colorkey(WHITE)
    pygame.draw.circle(surface, LIGHT_BLUE, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
    drop_particle.set_surface(surface.convert_alpha())
    drops.append(drop_particle)



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
        if event.type == new_drop_timer:
            add_drop()
    return True


# Aktualisierung des Spiels
def update_game():
    global drops
    new_drops = []
    for drop in drops:
        drop.apply_force(GRAVITY)
        drop.update()
        if drop.position[1] < HEIGHT:
            new_drops.append(drop)
    drops = new_drops
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(WHITE)
    for drop in drops:
        drop.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
    main()


