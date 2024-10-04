import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global clicks
    clicks = []
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
            clicks.append(pos)
    return True


# Aktualisierung des Spiels
def update_game():
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    last_pos = None
    for pos in clicks:
        if last_pos is not None:
            pygame.draw.line(screen, RED, last_pos, pos, 2)
        last_pos = pos
    pygame.display.flip()


# Start des Programms
main()