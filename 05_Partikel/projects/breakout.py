from importlib.metadata import pass_none

import pygame
import random
from particle import Particle

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
SIZE = (WIDTH, HEIGHT)
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

BALL_RADIUS = 8


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    random.seed()
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    init_clock()
    init_new_game()
    pygame.display.set_caption("Breakout")
    return screen

def init_new_game():
    global ball, paddle, game_over
    init_bricks()
    init_paddle()
    init_ball()
    game_over = False



# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Tropfen
def init_bricks():
    global bricks
    bricks = []
    for x in range(BRICK_WIDTH, WIDTH, BRICK_WIDTH):
        for y in range(BRICK_HEIGHT, HEIGHT // 4, BRICK_HEIGHT):
            brick = Particle(x, y)
            surface = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            surface.fill(color)
            brick.set_surface(surface)
            bricks.append(brick)


def init_ball():
    global ball
    ball = Particle(WIDTH // 2, HEIGHT // 2)
    vx = random.randint(1, 2) * random.choice([-1, 1])
    vy = random.randint(1, 3)
    ball.velocity = (vx, vy)
    surface = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
    surface.fill(WHITE)
    surface.set_colorkey(WHITE)
    pygame.draw.circle(surface, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
    ball.set_surface(surface)


def init_paddle():
    global paddle
    paddle = Particle(WIDTH // 2, HEIGHT - PADDLE_HEIGHT)
    surface = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
    surface.fill(BLUE)
    paddle.set_surface(surface)


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
    global ball
    global game_over
    global bricks

    if not game_over:
        update_paddle()
        ball.update()
        check_bounce()
        bricks = [brick for brick in bricks if not check_hit_brick(brick)]
        if len(bricks) == 0:
            game_over = True
        if ball.position[1] > HEIGHT:
            game_over = True
    else:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            init_new_game()

    return True


def check_bounce():
    global ball
    if ball.position[0] < 0 or ball.position[0] > WIDTH:
        ball.velocity = (-ball.velocity[0], ball.velocity[1])
    if ball.position[1] < 0:
        ball.velocity = (ball.velocity[0], -ball.velocity[1])

    rect = pygame.Rect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
    rect.center = paddle.position
    distance_x, distance_y = circle_rect_distance(ball.position, rect)
    if distance_x ** 2 + distance_y ** 2 < BALL_RADIUS **2:
        if ball.position[1] < rect.top:
            # Hit from Top
            ball.velocity = (ball.velocity[0], -ball.velocity[1])
        elif ball.position[0] < rect.left or ball.position[0] > rect.right:
            # Hit from Left or Right
            ball.velocity = (-ball.velocity[0], -ball.velocity[1])


def update_paddle():
    global paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.position[0] > PADDLE_WIDTH // 2:
        paddle.position = (paddle.position[0] - 5, paddle.position[1])
    if keys[pygame.K_RIGHT] and paddle.position[0] < WIDTH - PADDLE_WIDTH // 2:
        paddle.position = (paddle.position[0] + 5, paddle.position[1])

def check_hit_brick(brick):
    global ball
    rect = pygame.Rect(0, 0, BRICK_WIDTH, BRICK_HEIGHT)
    rect.center = brick.position
    distance_x, distance_y = circle_rect_distance(ball.position, rect)
    if distance_x ** 2 + distance_y ** 2 >= BALL_RADIUS **2:
        return False
    random_drift = 1 + random.random() * 0.1
    if ball.position[1] < rect.top or ball.position[1] > rect.bottom:
        # Hit from Top or Bottom
        ball.velocity = (- ball.velocity[0], ball.velocity[1] * random_drift)
    else:
        # Hit from Left or Right
        ball.velocity = (ball.velocity[0] * random_drift, -ball.velocity[1])
    return True

def circle_rect_distance(circle_position, rect):
    circle_x, circle_y = circle_position
    closest_x, closest_y = closest_pos_on_rect(circle_position, rect)
    distance_x = circle_x - closest_x
    distance_y = circle_y - closest_y
    return distance_x, distance_y

def closest_pos_on_rect(circle_position, rect):
    circle_x, circle_y = circle_position
    closest_x = max(rect.left, min(circle_x, rect.right))
    closest_y = max(rect.top, min(circle_y, rect.bottom))
    return closest_x, closest_y

# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(WHITE)
    for brick in bricks:
        brick.draw(screen)
    paddle.draw(screen)
    ball.draw(screen)

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

if __name__ == "__main__":
    main()


