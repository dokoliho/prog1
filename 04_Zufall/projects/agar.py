import pygame
import random

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELL_RADIUS = 5
PELLET_RADIUS = 2
PELLET_COUNT = 100
SPEED = 3
KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global pellets
    global cell
    global keys_pressed
    global clock
    random.seed()
    cell = (WIDTH // 2, HEIGHT // 2, CELL_RADIUS)
    keys_pressed = [False, False, False, False]
    pellets = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(PELLET_COUNT)]
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


# Event-Behandlung
def event_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            handle_key_event(event)
    return True


def handle_key_event(event):
    global keys_pressed
    new_value = (event.type == pygame.KEYDOWN)
    if event.key == pygame.K_UP:
        keys_pressed[KEY_UP] = new_value
    if event.key == pygame.K_DOWN:
        keys_pressed[KEY_DOWN] = new_value
    if event.key == pygame.K_LEFT:
        keys_pressed[KEY_LEFT] = new_value
    if event.key == pygame.K_RIGHT:
        keys_pressed[KEY_RIGHT] = new_value


# Aktualisierung des Spiels
def update_game():
    update_cell_position()
    update_cell_size()
    return True


def update_cell_size():
    global cell, pellets
    new_pellets = [pellet for pellet in pellets
                   if not test_circle_collision(cell[0], cell[1], cell[2],
                                                pellet[0], pellet[1], PELLET_RADIUS)]
    cell = (cell[0], cell[1], cell[2] + len(pellets) - len(new_pellets))
    pellets = new_pellets


def update_cell_position():
    global cell
    if keys_pressed[KEY_UP]:
        cell = (cell[0], (cell[1] - SPEED) % HEIGHT, cell[2])
    if keys_pressed[KEY_DOWN]:
        cell = (cell[0], (cell[1] + SPEED) % HEIGHT, cell[2])
    if keys_pressed[KEY_LEFT]:
        cell = ((cell[0] - SPEED) % WIDTH, cell[1], cell[2])
    if keys_pressed[KEY_RIGHT]:
        cell = ((cell[0] + SPEED) % WIDTH, cell[1], cell[2])


def test_circle_collision(c1x, c1y, c1r, c2x, c2y, c2r):
    return (c1x - c2x) ** 2 + (c1y - c2y) ** 2 <= (c1r + c2r) ** 2


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (cell[0], cell[1]), cell[2])
    for pellet in pellets:
        pygame.draw.circle(screen, BLUE, pellet, PELLET_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
