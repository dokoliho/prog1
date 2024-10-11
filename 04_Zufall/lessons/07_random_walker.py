import pygame
import random

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 10
SPEED = 3


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global position
    global clock
    position = (WIDTH // 2, HEIGHT // 2)
    random.seed()
    clock = pygame.time.Clock()
    pygame.init()
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
    global keys_pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Aktualisierung des Spiels
def update_game():
    global position
    delta_x = random.randint(-1, 1)
    delta_y = random.randint(-1, 1)
    new_x = (position[0] + delta_x * SPEED) % WIDTH
    new_y = (position[1] + delta_y * SPEED) % HEIGHT
    position = (new_x, new_y)
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
