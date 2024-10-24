import pygame
import random

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 2

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    random.seed()
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global stars, clock
    stars = []
    pygame.init()
    clock = pygame.time.Clock()
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
    return True


# Aktualisierung des Spiels
def update_game():
    global stars
    new_star = (random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3))
    stars.append(new_star)
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for star in stars:
        pygame.draw.circle(screen, WHITE, (star[0], star[1]), star[2] )
    pygame.display.flip()


# Start des Programms
main()