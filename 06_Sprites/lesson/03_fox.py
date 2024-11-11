import pygame
import random
from game import Game
from particle import Particle

WIDTH = 640
HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEXT_IMAGE = 200
SPEED = 50

class Fox(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        surface = pygame.image.load("fox.png")
        self.images = []
        for row in range(4):
            for column in range(4):
                rect = pygame.Rect(column * 256, row * 256, 256, 256)
                image = pygame.Surface(rect.size).convert()
                image.blit(surface, (0, 0), rect)
                color = image.get_at((0, 0))
                image.set_colorkey(color, pygame.RLEACCEL)
                image = pygame.transform.scale(image, (64, 64))
                self.images.append(image.convert_alpha())
        self.sequence = 0
        self.timer = 0

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer > NEXT_IMAGE/1000:
            self.sequence = (self.sequence + 1) % 4
            self.timer = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity = (0, -SPEED)
        elif keys[pygame.K_DOWN]:
            self.velocity = (0, SPEED)
        elif keys[pygame.K_LEFT]:
            self.velocity = (-SPEED, 0)
        elif keys[pygame.K_RIGHT]:
            self.velocity = (SPEED, 0)
        super().update(delta_time)



    def draw(self, screen):
        sequence = [1]
        if self.velocity[0] < 0:
            sequence = [4, 5, 6, 7]
        elif self.velocity[0] > 0:
            sequence = [8, 9, 10, 11]
        elif self.velocity[1] < 0:
            sequence = [12, 13, 14, 15]
        elif self.velocity[1] > 0:
            sequence = [0, 1, 2, 3]
        index = sequence[self.sequence % len(sequence)]
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
