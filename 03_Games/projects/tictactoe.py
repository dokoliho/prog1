import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = WIDTH
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SEGMENT = WIDTH // 3
FONT_SIZE = SEGMENT // 2
FONT_NAME = None   # None = default font
FPS = 30

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global cells
    global clock
    global font
    cells = []
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
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
    global cells
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0] // SEGMENT
            y = pos[1] // SEGMENT
            free = True
            for cell in cells:
                if cell[0] == x and cell[1] == y:
                    free = False
            if free:
                cells.append((x, y))
    return True


# Aktualisierung des Spiels
def update_game():
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.line(screen, RED, (0, SEGMENT), (WIDTH, SEGMENT), 4)
    pygame.draw.line(screen, RED, (0, 2*SEGMENT), (WIDTH, 2*SEGMENT), 4)
    pygame.draw.line(screen, RED, (SEGMENT, 0), (SEGMENT, HEIGHT), 4)
    pygame.draw.line(screen, RED, (2*SEGMENT, 0), (2*SEGMENT, HEIGHT), 4)

    player = 0
    for cell in cells:
        if player == 0:
            text = font.render("X", True, WHITE)
        else:
            text = font.render("0", True, WHITE)
        text_rect = text.get_rect(center=(cell[0] * SEGMENT + SEGMENT // 2,
                                          cell[1] * SEGMENT + SEGMENT // 2))
        screen.blit(text, text_rect)
        player = (player + 1) % 2
    pygame.display.flip()


# Start des Programms
main()