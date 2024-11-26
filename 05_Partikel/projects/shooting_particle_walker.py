import pygame
import random

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FRICTION = 0.3
FPS = 20
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

CIRCLE_RADIUS = 10
SHOT_RADIUS = 2
FORCE = 2
SHOT_FORCE = 10

class Particle:
    def __init__(self, x, y):
        self.position = (x, y)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.surface = None

    def set_surface(self, surface):
        self.surface = surface

    def apply_force(self, force):
        self.acceleration = (self.acceleration[0] + force[0], self.acceleration[1] + force[1])

    def update(self):
        self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.acceleration = (0, 0)

    def draw(self, screen):
        if self.surface is not None:
            blit_positon = (self.position[0] - self.surface.get_width()/2,
                            self.position[1] - self.surface.get_height()/2)
            screen.blit(self.surface, blit_positon)


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
    init_circle()
    init_shots()
    return screen


def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung des Kreises
def init_circle():
    global walker, last_direction
    walker = Particle(WIDTH // 2, HEIGHT // 2)
    last_direction = (1, 0)
    surface = pygame.Surface((CIRCLE_RADIUS*2, CIRCLE_RADIUS*2))
    pygame.draw.circle(surface, RED, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
    walker.set_surface(surface.convert_alpha())


def init_shots():
    global shots
    shots = []

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
    global last_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                add_shot()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        last_direction = (-1, 0)
        walker.apply_force((-FORCE, 0))
    if keys[pygame.K_RIGHT]:
        last_direction = (1, 0)
        walker.apply_force((FORCE, 0))
    if keys[pygame.K_UP]:
        last_direction = (0, -1)
        walker.apply_force((0, -FORCE))
    if keys[pygame.K_DOWN]:
        last_direction = (0, 1)
        walker.apply_force((0, FORCE))
    return True


def add_shot():
    global shots
    shot = Particle(walker.position[0], walker.position[1])
    surface = pygame.Surface((SHOT_RADIUS*2, SHOT_RADIUS*2))
    pygame.draw.circle(surface, YELLOW, (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
    shot.set_surface(surface.convert_alpha())
    shot.apply_force((last_direction[0] * SHOT_FORCE, last_direction[1] * SHOT_FORCE))
    shots.append(shot)

# Aktualisierung des Spiels
def update_game():
    global walker, shots
    walker.apply_force((walker.velocity[0] * -FRICTION, walker.velocity[1] * -FRICTION))
    walker.update()
    shots = [shot for shot in shots if shot_alive_after_update(shot)]
    return True


def shot_alive_after_update(shot):
    shot.update()
    return shot.position[1] > 0 and shot.position[1] < HEIGHT and shot.position[0] > 0 and shot.position[0] < WIDTH


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for shot in shots:
        shot.draw(screen)
    walker.draw(screen)
    pygame.display.flip()


# Start des Programms
main()
