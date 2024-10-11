import pygame
import random

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SIZE_BLUE = 20
SIZE_GREEN = 30
SPEED = 3


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global rect_green
    global rect_blue
    global movement_green
    global movement_blue
    global clock
    random.seed()
    rect_green = pygame.Rect((random.randint(0, WIDTH // 2 - SIZE_GREEN),
                              random.randint(0, HEIGHT // 2) - SIZE_GREEN),
                             (SIZE_GREEN, SIZE_GREEN))
    movement_green = [0, 0]
    rect_blue = pygame.Rect((WIDTH // 2 + random.randint(0, WIDTH // 2),
                             HEIGHT // 2 + random.randint(0, HEIGHT // 2),
                             SIZE_BLUE, SIZE_BLUE))
    movement_blue = [0, 0]
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
    global rect_green
    global movement_green
    global rect_blue
    global movement_blue

    movement_green = update_movement(movement_green)
    movement_blue = update_movement(movement_blue)
    rect_green = update_rect(movement_green, rect_green)
    rect_blue = update_rect(movement_blue, rect_blue)
    if rect_green.colliderect(rect_blue):
        return False
    return True


def update_rect(movement, rect):
    rect.x = (rect.x + movement[0] * SPEED) % WIDTH
    rect.y = (rect.y + movement[1] * SPEED) % HEIGHT
    return rect


def update_movement(movement):
    if random.randint(0, 100) < 10:
        movement[0] = random.randint(-1, 1)
    if random.randint(0, 100) < 5:
        movement[1] = random.randint(-1, 1)
    return movement

# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, rect_green)
    pygame.draw.rect(screen, BLUE, rect_blue)
    pygame.display.flip()


# Start des Programms
main()
