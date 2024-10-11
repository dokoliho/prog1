import pygame
import random



# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
COLUMN_COUNT = 10
COLUMN_WIDTH = WIDTH / COLUMN_COUNT
FPS = 30


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global counts
    global clock
    counts = [0] * COLUMN_COUNT
    pygame.init()
    clock = pygame.time.Clock()
    random.seed()
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
    global counts

    index = random.randint(0, COLUMN_COUNT-1)
    counts[index] += 1
    if counts[index] == HEIGHT:
        return False
    return True





# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for i in range(COLUMN_COUNT):
        x = i * COLUMN_WIDTH
        pygame.draw.rect(screen, RED, (x, HEIGHT - counts[i], COLUMN_WIDTH, counts[i]))
    pygame.display.flip()


# Start des Programms
main()
