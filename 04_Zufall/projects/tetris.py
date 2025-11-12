import pygame
import random

# Festlegung der Konstanten
SPEED = 4
FPS = 25
WHITE = (255, 255, 255)
BLOCK_SIZE = 7 * SPEED
WIDTH = 14 * BLOCK_SIZE
HEIGHT = WIDTH
SIZE = (WIDTH, HEIGHT)

BLOCK1 = (BLOCK_SIZE, BLOCK_SIZE) # Einer-Block
BLOCK2 = (2 * BLOCK_SIZE, BLOCK_SIZE) # horizontaler Zweier-Block
BLOCK3 = (BLOCK_SIZE, 2 * BLOCK_SIZE) # vertikaler Zweier-Block
BLOCK4 = (2 * BLOCK_SIZE, 2 * BLOCK_SIZE) # Vierer-Block
SHAPES = [BLOCK1, BLOCK2, BLOCK3, BLOCK4]


# Hauptfunktion mit Standardstruktur eines Pygame
def main():
    screen = init_game()
    game_loop(screen)
    exit_game()


# Initialisierung von Pygame
def init_game():
    global retired_blocks
    global active_block
    global clock
    random.seed()
    retired_blocks = [] # Liste der Blöcke, die nicht mehr fallen
    active_block = create_block() # Der fallende Block
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


# Event-Behandlung
def event_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Aktualisierung des Spiels
def update_game():
    check_hit_bottom()
    if active_block is None:
        return False
    check_hit_block()
    if active_block is None:
        return False
    move_active_block()
    return True


def check_hit_bottom():
    global active_block, retired_blocks
    shape = active_block[0]
    if active_block[2] + shape[1] >= HEIGHT:
        retired_blocks.append(active_block)
        active_block = create_block()


def check_hit_block():
    global active_block, retired_blocks
    if is_blocked(active_block):
        retired_blocks.append(active_block)
        active_block = create_block()


def is_blocked(block):
    block_shape = block[0]
    for retired_block in retired_blocks:
        retired_block_shape = retired_block[0]
        if is_block_hit_from_top(block[1], block[2], block_shape,
                                 retired_block[1], retired_block[2], retired_block_shape):
            return True
    return False


def is_block_hit_from_top(x1, y1, shape1, x2, y2, shape2):
    if x1 >= x2 + shape2[0] or x2 >= x1 + shape1[0]:
        return False
    if y1 + shape1[1] < y2:
        return False
    return True


def move_active_block():
    global active_block
    shape = active_block[0]
    # Fallen
    active_block = (shape, active_block[1], active_block[2] + SPEED, active_block[3])
    # Seitwärts bewegen
    on_left_key()
    on_right_key()


def on_right_key():
    global active_block
    shape = active_block[0]
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] and active_block[1] + shape[0] <= WIDTH - BLOCK_SIZE:
        for retired_block in retired_blocks:
            if would_move_into_block(active_block, retired_block, +BLOCK_SIZE):
                break
        else:
            active_block = (shape, active_block[1] + BLOCK_SIZE, active_block[2], active_block[3])


def on_left_key():
    global active_block
    shape = active_block[0]
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and active_block[1] >= BLOCK_SIZE:
        for retired_block in retired_blocks:
            if would_move_into_block(active_block, retired_block, -BLOCK_SIZE):
                break
        else:
            active_block = (shape, active_block[1] - BLOCK_SIZE, active_block[2], active_block[3])


def would_move_into_block(block1, block2, movement):
    shape1 = block1[0]
    shape2 = block2[0]
    if block1[1] + movement >= block2[1] + shape2[0] or block2[1] >= block1[1] + shape1[0] + movement:
        return False
    if block1[2] + shape1[1] < block2[2]:
        return False
    return True

def create_block():
    block = (random.choice(SHAPES), WIDTH // 2, 0,
            (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    if is_blocked(block):
        return None
    return block

# Zeichnen des Spiels
def draw_game(screen):
    screen.fill(WHITE)
    draw_block(screen, active_block)
    for block in retired_blocks:
        draw_block(screen, block)
    pygame.display.flip()

def draw_block(screen, block):
    shape = block[0]
    color = block[3]
    pygame.draw.rect(screen, color, (block[1], block[2], shape[0], shape[1]))

# Start des Programms
main()
