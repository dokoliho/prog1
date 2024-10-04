import pygame

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 5
MAX_SPEED = 30
FRICTION = 0.97


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global position
    global speed
    global clock
    global pushed
    position = (WIDTH // 2, HEIGHT // 2)
    speed = (0.0, 0.0)
    clock = pygame.time.Clock()
    pushed = False
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
        if not pushed and event.type == pygame.MOUSEBUTTONUP:
            button_pushed()
    return True


def button_pushed():
    global speed, pushed
    mouse_pos = pygame.mouse.get_pos()
    delta_x = mouse_pos[0] - position[0]
    delta_y = mouse_pos[1] - position[1]
    speed = (MAX_SPEED * delta_x / WIDTH, MAX_SPEED * delta_y / HEIGHT)
    pushed = True


# Aktualisierung des Spiels
def update_game():
    if pushed:
        calc_new_position()
        calc_new_speed()
    return True


def calc_new_speed():
    global speed, pushed
    speed = (speed[0] * FRICTION, speed[1] * FRICTION)
    if abs(speed[0]) < 0.1 and abs(speed[1]) < 0.1:
        pushed = False
        speed = (0.0, 0.0)


def calc_new_position():
    global speed, position
    position = (position[0] + speed[0], position[1] + speed[1])
    if position[0] < CIRCLE_RADIUS or position[0] + CIRCLE_RADIUS >= WIDTH:
        speed = (-speed[0], speed[1])
        position = (position[0] + speed[0], position[1] + speed[1])
    if position[1] < CIRCLE_RADIUS or position[1] + CIRCLE_RADIUS >= HEIGHT:
        speed = (speed[0], -speed[1])
        position = (position[0] + speed[0], position[1] + speed[1])


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(GREEN)
    pygame.draw.circle(screen, BLACK, position, CIRCLE_RADIUS)
    if not pushed:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 0 and mouse_pos[0] < WIDTH-1 and mouse_pos[1] > 0 and mouse_pos[1] < HEIGHT-1:
            pygame.draw.line(screen, RED, position, mouse_pos, 2)
    pygame.display.flip()



# Start des Programms
main()
