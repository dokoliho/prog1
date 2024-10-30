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

CIRCLE_RADIUS = 10
FORCE = 2

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
    return screen


def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung des Kreises
def init_circle():
    global particle
    particle = Particle(WIDTH // 2, HEIGHT // 2)
    surface = pygame.Surface((CIRCLE_RADIUS*2, CIRCLE_RADIUS*2))
    pygame.draw.circle(surface, RED, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
    particle.set_surface(surface.convert_alpha())


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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        particle.apply_force((-FORCE, 0))
    if keys[pygame.K_RIGHT]:
        particle.apply_force((FORCE, 0))
    if keys[pygame.K_UP]:
        particle.apply_force((0, -FORCE))
    if keys[pygame.K_DOWN]:
        particle.apply_force((0, FORCE))
    return True


# Aktualisierung des Spiels
def update_game():
    global particle
    particle.apply_force((particle.velocity[0] * -FRICTION, particle.velocity[1] * -FRICTION))
    particle.update()
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    particle.draw(screen)
    pygame.display.flip()


# Start des Programms
main()
