import pygame
import random
from particle import Particle

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 60

INTENSITY = 50
SPREAD = 5
MAX_BURN_RATE = 4
START_ACTIVITY = 50
MAX_SPEED = 7

BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
GREY = (100, 100, 100)


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
    init_flame()
    pygame.display.set_caption("Flamme")
    return screen


# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Flammenpartikel
def init_flame():
    global particles
    particles = []
    for _ in range(INTENSITY):
        particles.append(new_particle())


# Initialisierung eines Flammenpartikels
def new_particle():
    global particles
    x = WIDTH // 2 + random.randint(-SPREAD, SPREAD)
    y = HEIGHT // 4 * 3 + random.randint(1, SPREAD)
    particle = Particle(x, y)
    particle.burn_rate = random.randint(1, MAX_BURN_RATE)
    particle.activity = START_ACTIVITY
    return particle


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
    return True


# Aktualisierung des Spiels
def update_game():
    global particles
    new_particles = []
    for particle in particles:
        activity = particle.activity // 10
        particle.position = (particle.position[0] + random.randint(-activity, activity),
                             particle.position[1] - ( MAX_SPEED  - activity))
        particle.activity -= particle.burn_rate
        if particle.activity <= 0:
            new_particles.append(new_particle())
        else:
            new_particles.append(particle)
    particles = new_particles
    return True


# Zeichnen der Flamme
def draw_game(screen):
    screen.fill(BLACK)
    for particle in particles:
        color = particle_color(particle.activity)
        pygame.draw.circle(screen, color, particle.position, particle.activity // 10 )
    pygame.display.flip()


def particle_color(activity):
    if activity >= 30:
        color = RED
    elif activity >= 20:
        color = ORANGE
    else:
        color = GREY
    return color


if __name__ == "__main__":
    main()


