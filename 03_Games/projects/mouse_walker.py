import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 10
FPS = 30


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global position
    global speed
    global acceleration
    global clock
    position = (WIDTH // 2, HEIGHT // 2)
    speed = (0, 0)
    acceleration = (0, 0)
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
    global position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Aktualisierung des Spiels
def update_game():
    global position
    global speed
    global acceleration

    mouse_pos = pygame.mouse.get_pos()
    delta_x = (mouse_pos[0] - position[0])
    delta_y = (mouse_pos[1] - position[1])
    acceleration = (delta_x/WIDTH, delta_y/HEIGHT)
    speed_x =   min(5, max(speed[0] + acceleration[0], -5))
    speed_y =   min(5, max(speed[1] + acceleration[1], -5))
    speed = (speed_x, speed_y)
    position = (position[0] + speed[0], position[1] + speed[1])
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, position, CIRCLE_RADIUS)
    pygame.display.flip()


# Start des Programms
main()
