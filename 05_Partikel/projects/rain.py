import pygame
import random
from particle import Particle

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 60
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

CIRCLE_RADIUS = 4
GRAVITY = (0, 0.1)
DROP_RATE = 10 # per second
DENSITY = 2
WIND_INCREASE = 1

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
    init_drops()
    pygame.display.set_caption("Rain")
    return screen


# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Nahrung
def init_drops():
    global drops, density, wind, drop_surface
    drops = []
    density = DENSITY
    wind = (0, 0)
    drop_surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2))
    pygame.draw.circle(drop_surface, BLUE, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
    drop_surface = drop_surface.convert_alpha()
    add_drops()


def add_drops():
    global drops, last_drop
    for _ in range(density):
        drop = Particle(random.randint(0, WIDTH), 0)
        drop.set_surface(drop_surface)
        drop.apply_force(wind)
        drops.append(drop)
    last_drop = pygame.time.get_ticks()     # Time of last drop in milliseconds



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
    global density, wind
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                density += 1
            if event.key == pygame.K_DOWN:
                density -= 1
            if event.key == pygame.K_LEFT:
                wind = (wind[0] - WIND_INCREASE, wind[1])
                for drop in drops:
                    drop.apply_force((-WIND_INCREASE, 0))
            if event.key == pygame.K_RIGHT:
                wind = (wind[0] + WIND_INCREASE, wind[1])
                for drop in drops:
                    drop.apply_force((WIND_INCREASE, 0))

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
    if pygame.time.get_ticks() - last_drop > 1000 // DROP_RATE:
        add_drops()
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for drop in drops:
        drop.draw(screen)
    pygame.display.flip()


# Start des Programms
main()


