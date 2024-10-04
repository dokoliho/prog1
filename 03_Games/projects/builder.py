import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLOCKSIZE = 20
FPS = 30

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global blocks
    global clock
    blocks = []
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
    global clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0] // BLOCKSIZE * BLOCKSIZE
            y = pos[1] // BLOCKSIZE * BLOCKSIZE
            blocks.append((x, y))
    return True


# Aktualisierung des Spiels
def update_game():
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for block in blocks:
        block_shape = (block[0], block[1], BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(screen, YELLOW, block_shape)
        pygame.draw.rect(screen, RED, block_shape, 1)
    pygame.display.flip()


# Start des Programms
main()