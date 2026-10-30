import pygame
import math
import datetime

# Festlegung der Konstanten
WIDTH = 320
HEIGHT = 240
SIZE = (WIDTH, HEIGHT)
DISTANCE = 10
CIRCLE_RADIUS = HEIGHT//2 - DISTANCE
NUMBER_RADIUS = CIRCLE_RADIUS * 0.9
HOURS_LENGTH = NUMBER_RADIUS * 0.6
MINUTES_LENGTH = NUMBER_RADIUS * 0.8
SECONDS_LENGTH = NUMBER_RADIUS * 0.9
FONT_SIZE = 20
FONT_NAME = None   # None = default font
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 1


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global clock
    global font
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Aktualisierung des Spiels
def update_game():
    global hours_angle
    global minutes_angle
    global seconds_angle
    now = datetime.datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second
    hours_angle = (hours * 60 + minutes) / 720 * 2 * math.pi
    minutes_angle = minutes / 60 * 2 * math.pi
    seconds_angle = seconds / 60 * 2 * math.pi
    return True


# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(BLACK)
    position = (WIDTH//2, HEIGHT//2)
    draw_dial(screen, position)
    draw_hands(screen, position)
    pygame.display.flip()


# Zeichnen des Ziffernblatts
def draw_dial(screen, position):
    # Rand
    pygame.draw.circle(screen, WHITE, position, CIRCLE_RADIUS, 1)
    # Ziffern
    for i in range(12):
        angle = i * (2 * math.pi) / 12
        y = math.cos(angle) * NUMBER_RADIUS * -1
        x = math.sin(angle) * NUMBER_RADIUS
        text = font.render(str(i or 12), True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2 + x, HEIGHT // 2 + y))
        screen.blit(text, text_rect)


# Zeichnen der Zeiger
def draw_hands(screen, position):
    draw_hand(screen, position, hours_angle, HOURS_LENGTH, WHITE, 4)
    draw_hand(screen, position, minutes_angle, MINUTES_LENGTH, WHITE, 2)
    draw_hand(screen, position, seconds_angle, SECONDS_LENGTH, RED, 1)


# Zeichnen eines einzelnen Zeigers
def draw_hand(screen, position, angle, length, color, width):
    end_pos = (position[0] + math.sin(angle) * length, position[1] + math.cos(angle) * length * -1)
    pygame.draw.line(screen, color, position, end_pos, width)


# Start des Programms
main()
