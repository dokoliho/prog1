import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 10


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global position
    position = (WIDTH // 2, HEIGHT // 2)
    pygame.init()
    pygame.display.set_caption('Walker')
    return pygame.display.set_mode(SIZE)


# Game-Loop
def game_loop(screen):
    while True:
        if event_handling() == False:
            break
        if update_game() == False:
            break
        draw_game(screen)

# Beenden von Pygame
def exit_game():
    pygame.quit()


# Behandlung der Events
def event_handling():
    global position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                position = (position[0], position[1] - 1)
            if event.key == pygame.K_DOWN:
                position = (position[0], position[1] + 1)
            if event.key == pygame.K_LEFT:
                position = (position[0] - 1, position[1])
            if event.key == pygame.K_RIGHT:
                position = (position[0] + 1, position[1])
    return True


# Aktualisierung des Spiels
def update_game():
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
