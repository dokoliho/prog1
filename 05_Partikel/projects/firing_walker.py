import pygame
import random
import math
from particle import Particle

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CIRCLE_RADIUS = 10
SHOT_RADIUS = 5
FIRE_RATE = 10
SHOT_SPEED = 5
KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3
SPEED = 3


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global position
    global keys_pressed
    global clock
    global shots
    global last_shot
    position = (WIDTH // 2, HEIGHT // 2)
    shots = []
    last_shot= pygame.time.get_ticks()
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Firing Walker")
    return pygame.display.set_mode(SIZE)


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
    update_position()
    update_shots()
    return True


def update_position():
    global position
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        position = (position[0], position[1] - SPEED)
    if keys_pressed[pygame.K_DOWN]:
        position = (position[0], position[1] + SPEED)
    if keys_pressed[pygame.K_LEFT]:
        position = (position[0] - SPEED, position[1])
    if keys_pressed[pygame.K_RIGHT]:
        position = (position[0] + SPEED, position[1])


def update_shots():
    global shots
    if pygame.time.get_ticks() - last_shot > 1000 // FIRE_RATE:
        new_shot(shots)
    new_shots = []
    for shot in shots:
        shot.update()
        if shot.position[0] < 0 or shot.position[0] > WIDTH or shot.position[1] < 0 or shot.position[1] > HEIGHT:
            continue
        new_shots.append(shot)
    shots = new_shots


def new_shot(shots):
    global last_shot
    last_shot = pygame.time.get_ticks()
    angle = random.randint(0, 360)
    angle = math.radians(angle)
    dx = SHOT_SPEED * math.cos(angle)
    dy = SHOT_SPEED * math.sin(angle)
    shot = Particle(position[0] + math.cos(angle) * CIRCLE_RADIUS,
                    position[1] + math.sin(angle) * CIRCLE_RADIUS)
    shot.velocity = (dx, dy)
    shots.append(shot)


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for shot in shots:
        pygame.draw.circle(screen, YELLOW, shot.position, SHOT_RADIUS)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
if __name__ == '__main__':
    main()
