import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 10
SPEED = 5


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
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Walker Improved')
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
    global position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        position = (position[0], position[1] - SPEED)
    if keys[pygame.K_DOWN]:
        position = (position[0], position[1] + SPEED)
    if keys[pygame.K_LEFT]:
        position = (position[0] - SPEED, position[1])
    if keys[pygame.K_RIGHT]:
        position = (position[0] + SPEED, position[1])
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
