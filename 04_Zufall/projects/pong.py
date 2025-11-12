import pygame
import random

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30
FONT_NAME = None   # None = default font
PAD_SIZE = (10, 50)
BALL_RADIUS = 10
MIN_BALL_SPEED = 3
MAX_BALL_SPEED = 5
PAD_SPEED = 3
DIRECTIONS = [-1, 1]
LEFT_KEY_UP = pygame.K_w
LEFT_KEY_DOWN = pygame.K_s
RIGHT_KEY_UP = pygame.K_UP
RIGHT_KEY_DOWN = pygame.K_DOWN

# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global left_pad, right_pad, ball, clock, left_score, right_score, font
    random.seed()
    left_pad = (10, HEIGHT // 2)
    right_pad = (WIDTH - 10 -PAD_SIZE[0], HEIGHT // 2)
    new_ball()
    left_score = 0
    right_score = 0
    clock = pygame.time.Clock()
    pygame.init()
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    return pygame.display.set_mode(SIZE)


def new_ball():
    global ball
    direction1 = random.choice(DIRECTIONS)
    direction2 = random.choice(DIRECTIONS)
    ball = (WIDTH // 2, HEIGHT // 2,
            random.randint(MIN_BALL_SPEED, MAX_BALL_SPEED) * direction1,
            random.randint(MIN_BALL_SPEED, MAX_BALL_SPEED) * direction2)


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
    update_ball_position()
    update_pad_positions()
    return True


def update_ball_position():
    global ball, left_score, right_score

    ball = (ball[0] + ball[2], ball[1] + ball[3], ball[2], ball[3])

    if ball[1] - BALL_RADIUS <= 0 or ball[1] + BALL_RADIUS >= HEIGHT:
        ball = (ball[0], ball[1], ball[2], -ball[3])

    if ball[0] <= left_pad[0] + PAD_SIZE[0]:
        if left_pad[1] - PAD_SIZE[1] // 2 <= ball[1] <= left_pad[1] + PAD_SIZE[1] // 2:
            ball = (ball[0], ball[1], -ball[2], ball[3])

    if ball[0] >= right_pad[0] - PAD_SIZE[0]:
        if right_pad[1] - PAD_SIZE[1] // 2 <= ball[1] <= right_pad[1] + PAD_SIZE[1] // 2:
            ball = (ball[0], ball[1], -ball[2], ball[3])

    if ball[0] <= 0:
        new_ball()
        right_score += 1

    if ball[0] >= WIDTH:
        new_ball()
        left_score += 1


def update_pad_positions():
    global left_pad, right_pad
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[LEFT_KEY_UP]:
        left_pad = (left_pad[0], max(0, left_pad[1] - PAD_SPEED))
    if keys_pressed[LEFT_KEY_DOWN]:
        left_pad = (left_pad[0], min(HEIGHT, left_pad[1] + PAD_SPEED))
    if keys_pressed[RIGHT_KEY_UP]:
        right_pad = (right_pad[0], max(0, right_pad[1] - PAD_SPEED))
    if keys_pressed[RIGHT_KEY_DOWN]:
        right_pad = (right_pad[0], min(HEIGHT, right_pad[1] + PAD_SPEED))


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball[0], ball[1]), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (left_pad[0], left_pad[1] - PAD_SIZE[1] // 2, PAD_SIZE[0], PAD_SIZE[1]))
    pygame.draw.rect(screen, WHITE, (right_pad[0] - PAD_SIZE[0], right_pad[1] - PAD_SIZE[1] // 2, PAD_SIZE[0], PAD_SIZE[1]))
    draw_score(screen)
    pygame.display.flip()

def draw_score(screen):
    text = font.render(f"{left_score:02}  : {right_score:02}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

# Start des Programms
main()
