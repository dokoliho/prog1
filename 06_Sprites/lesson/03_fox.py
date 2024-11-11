import pygame
import random
from game import Game
from particle import Particle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
        screen.blit(self.surface, blit_position)