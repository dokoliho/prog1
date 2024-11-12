import pygame
from game import Game
from delta_time_particle import DeltaTimeParticle

WIDTH = 640
HEIGHT = 480
WHITE = (255, 255, 255)
SPRITE_SHEET_SIZE = (1024, 1024)
SPRITE_SHEET_ROWS = 4
SPRITE_SHEET_COLUMNS = 4
SPRITE_WIDTH = SPRITE_SHEET_SIZE[0] // SPRITE_SHEET_COLUMNS
SPRITE_HEIGHT = SPRITE_SHEET_SIZE[1] // SPRITE_SHEET_ROWS
SPRITE_TARGET_SIZE = (64, 64)
BLACK = (0, 0, 0)

MS_PER_SPRITE_FRAME = 200
SPEED = 50

class Fox(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.read_sprite_sheet()
        self.current_sprite_frame_index = 0
        self.frame_time = 0

    def read_sprite_sheet(self):
        sprite_sheet = pygame.image.load("fox.png")
        self.images = []
        for row in range(SPRITE_SHEET_ROWS):
            for column in range(SPRITE_SHEET_COLUMNS):
                rect = pygame.Rect(column * SPRITE_WIDTH, row * SPRITE_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT)
                image = pygame.Surface(rect.size).convert()
                image.blit(sprite_sheet, (0, 0), rect)
                color = image.get_at((0, 0))
                image.set_colorkey(color)
                image = pygame.transform.scale(image, SPRITE_TARGET_SIZE)
                self.images.append(image.convert_alpha())

    def update(self, dt=1):
        self.frame_time += dt
        if self.frame_time > MS_PER_SPRITE_FRAME / 1000:
            self.current_sprite_frame_index = (self.current_sprite_frame_index + 1) % len(self.images)
            self.frame_time = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity = (0, -SPEED)
        elif keys[pygame.K_DOWN]:
            self.velocity = (0, SPEED)
        elif keys[pygame.K_LEFT]:
            self.velocity = (-SPEED, 0)
        elif keys[pygame.K_RIGHT]:
            self.velocity = (SPEED, 0)
        else:
            self.velocity = (0, 0)
        super().update(dt)



    def draw(self, screen):
        movement_image_index_sequence = [1] # Standing still
        if self.velocity[0] < 0:
            movement_image_index_sequence = [4, 5, 6, 7] # Moving left
        elif self.velocity[0] > 0:
            movement_image_index_sequence = [8, 9, 10, 11] # Moving right
        elif self.velocity[1] < 0:
            movement_image_index_sequence = [12, 13, 14, 15] # Moving up
        elif self.velocity[1] > 0:
            movement_image_index_sequence = [0, 1, 2, 3] # Moving down
        index = movement_image_index_sequence[self.current_sprite_frame_index % len(movement_image_index_sequence)]
        surface = self.images[index]
        blit_position = (self.position[0] - surface.get_width()/2,
                         self.position[1] - surface.get_height()/2)
        screen.blit(surface, blit_position)


class RunningFox(Game):
    def init_game_state(self):
        self.fox = Fox(WIDTH // 2, HEIGHT // 2)

    def handle_event(self, event):
        if not super().handle_event(event):
            return False
        return True

    def update_game(self):
        super().update_game()
        self.fox.update(self.dt)
        return True

    def draw_game(self):
        self.screen.fill(BLACK)
        self.fox.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = RunningFox("Running Fox")
    game.run()
