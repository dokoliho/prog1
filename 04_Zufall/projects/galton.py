import pygame
import random

# Festlegung der Konstanten
WIDTH = 200
HEIGHT = 320
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 40
ACCELERATION = 1
NAIL_RADIUS = 5
BALL_RADIUS = 3
BOX_HEIGHT = 120
BOX_WIDTH = 50

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    random.seed()
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global nails,  counts, ball, clock
    nails = [(100, 50), (75, 100), (125, 100), (50, 150), (100, 150), (150, 150)]
    counts = [0, 0, 0, 0]
    ball = (WIDTH // 2, 0, 0, 0)
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
    global ball, counts
    ball = (ball[0] + ball[2], ball[1] + ball[3], ball[2], ball[3] + ACCELERATION)
    for nail in nails:
        if test_circle_collision(nail[0], nail[1], NAIL_RADIUS, ball[0], ball[1], BALL_RADIUS):
            x_speed = random.choice([-2, 2])
            ball = (ball[0] + NAIL_RADIUS * x_speed // 2, ball[1], x_speed, 0)
    if ball[1] >= HEIGHT - BOX_HEIGHT:
        slot = ball[0] // BOX_WIDTH
        counts[slot] += 1
        ball = (WIDTH // 2, 0, 0, 0)
    return True

def test_circle_collision(c1x, c1y, c1r, c2x, c2y, c2r):
    return (c1x - c2x) ** 2 + (c1y - c2y) ** 2 <= (c1r + c2r) ** 2

# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for nail in nails:
        pygame.draw.circle(screen, WHITE, nail, NAIL_RADIUS)
    pygame.draw.circle(screen, RED, (ball[0], ball[1]), BALL_RADIUS)
    for i in range(4):
        pygame.draw.rect(screen, RED, (i * BOX_WIDTH + 1, HEIGHT - counts[i], BOX_WIDTH - 2, counts[i]))
    for i in range(1, 4):
        pygame.draw.rect(screen, WHITE, (i * BOX_WIDTH, HEIGHT - BOX_HEIGHT, 1, BOX_HEIGHT))
    pygame.display.flip()


# Start des Programms
main()