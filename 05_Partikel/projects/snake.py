import pygame
import random
from particle import Particle

# Festlegung der Konstanten
WIDTH = 400
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 3
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

CIRCLE_RADIUS = 10
SPEED = 20
FOOD_COUNT = 50


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global game_over
    random.seed()
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    init_clock()
    init_food()
    init_snake()
    pygame.display.set_caption("Snake")
    game_over = False
    return screen


# Initialisierung der Uhr
def init_clock():
    global clock
    clock = pygame.time.Clock()


# Initialisierung der Nahrung
def init_food():
    global food_items
    food_items = []
    for i in range(FOOD_COUNT):
        position = (random.randint(0, WIDTH // (2*CIRCLE_RADIUS)) * 2 * CIRCLE_RADIUS + CIRCLE_RADIUS,
                    random.randint(0, HEIGHT // (2*CIRCLE_RADIUS))* 2 * CIRCLE_RADIUS + CIRCLE_RADIUS)
        food_particle = Particle(position[0], position[1])
        surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2))
        pygame.draw.circle(surface, GREEN, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
        food_particle.set_surface(surface.convert_alpha())
        food_items.append(food_particle)


# Initialisierung der Schlange
def init_snake():
    global snake, snake_segment_surface
    snake_segment_surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2))
    pygame.draw.circle(snake_segment_surface, RED, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
    snake_segment_surface = snake_segment_surface.convert_alpha()
    head = Particle(WIDTH//2 + CIRCLE_RADIUS, HEIGHT//2 + CIRCLE_RADIUS)
    head.set_surface(snake_segment_surface)
    snake = [head]


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
    global snake
    head = snake[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if event.key == pygame.K_LEFT:
                head.velocity = (-SPEED, 0)
            if event.key == pygame.K_RIGHT:
                head.velocity = (SPEED, 0)
            if event.key == pygame.K_UP:
                head.velocity = (0, -SPEED)
            if event.key == pygame.K_DOWN:
                head.velocity = (0, SPEED)
    return True


# Aktualisierung des Spiels
def update_game():
    global snake, game_over

    # Keine Aktualisierung, wenn das Spiel vorbei ist
    if game_over:
        return True

    # Position des letzten Schlangenteils merken
    last_segment_position_x, last_segment_position_y = snake[-1].position

    # Schlangenbewegung
    update_snake()
    append_on_food_collision(last_segment_position_x, last_segment_position_y)

    # Spielende überprüfen
    if check_snake_collision() or check_edge_collision():
        game_over = True
    if len(food_items) == 0:
        game_over = True

    return True


# Aktualisierung der Positionen der Schlangenteile
def update_snake():
    global snake
    for i in range(len(snake) - 1, 0, -1):
        snake[i].position = snake[i - 1].position
    head = snake[0]
    head.update()


# Anhängen eines neuen Partikels an die Schlange
def append_on_food_collision(last_segment_position_x, last_segment_position_y):
    global food_items, snake
    head = snake[0]
    new_food = []
    for food in food_items:
        distance_square = (head.position[0] - food.position[0]) ** 2 + (head.position[1] - food.position[1]) ** 2
        if distance_square < (2 * CIRCLE_RADIUS) ** 2:
            new_segment = Particle(last_segment_position_x, last_segment_position_y)
            new_segment.set_surface(snake_segment_surface)
            snake.append(new_segment)
        else:
            new_food.append(food)
    food_items = new_food


# Kollision mit Spielfeldrand
def check_edge_collision():
    head = snake[0]
    return head.position[0] < 0 or head.position[0] > WIDTH or head.position[1] < 0 or head.position[1] > HEIGHT


# Kollision mit Schlangenkörper
def check_snake_collision():
    head = snake[0]
    for i in range(1, len(snake)):
        if head.position == snake[i].position:
            return True
    return False


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    for food in food_items:
        food.draw(screen)
    for segment in snake:
        segment.draw(screen)
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    pygame.display.flip()


# Start des Programms
main()