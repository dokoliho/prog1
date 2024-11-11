import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 10
KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3
SPEED = 5


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
    position = (WIDTH // 2, HEIGHT // 2)
    keys_pressed = [False, False, False, False]
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

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            new_value = (event.type == pygame.KEYDOWN)
            if event.key == pygame.K_UP:
                keys_pressed[KEY_UP] = new_value
            if event.key == pygame.K_DOWN:
                keys_pressed[KEY_DOWN] = new_value
            if event.key == pygame.K_LEFT:
                keys_pressed[KEY_LEFT] = new_value
            if event.key == pygame.K_RIGHT:
                keys_pressed[KEY_RIGHT] = new_value

    return True


# Aktualisierung des Spiels
def update_game():
    global position
    if keys_pressed[KEY_UP]:
        position = (position[0], position[1] - SPEED)
    if keys_pressed[KEY_DOWN]:
        position = (position[0], position[1] + SPEED)
    if keys_pressed[KEY_LEFT]:
        position = (position[0] - SPEED, position[1])
    if keys_pressed[KEY_RIGHT]:
        position = (position[0] + SPEED, position[1])
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
