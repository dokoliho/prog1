import pygame
import random
import math
from game import Game
from delta_time_particle import DeltaTimeParticle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 650
HEIGHT = 480
RADIUS = 5
PARTICLE_COUNT = 50
MARGIN = 75
MAX_SPEED = 120
MAX_FORCE = 200

class Avoider(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        surface = pygame.Surface((10, 10))
        surface.fill(BLACK)
        surface.set_colorkey(BLACK)
        pygame.draw.circle(surface, WHITE, (RADIUS, RADIUS), RADIUS)
        self.set_surface(surface.convert_alpha())
        angle = random.randint(0, 360)
        direction = math.radians(angle)
        speed = random.randint(MAX_SPEED // 4, MAX_SPEED)
        self.velocity = (math.cos(direction) * speed, math.sin(direction) * speed)

    def update(self, dt=1):
        super().update(dt)
        if self.position[0] < MARGIN:
            self.apply_force((MAX_FORCE, 0))
        if self.position[0] > WIDTH - MARGIN:
            self.apply_force((-MAX_FORCE, 0))
        if self.position[1] < MARGIN:
            self.apply_force((0, MAX_FORCE))
        if self.position[1] > HEIGHT - MARGIN:
            self.apply_force((0, -MAX_FORCE))
        if (self.position[0] > MARGIN and self.position[0] < WIDTH - MARGIN and
                self.position[1] > MARGIN and self.position[1] < HEIGHT - MARGIN):
            dx = MAX_SPEED - abs(self.velocity[0])
            dy = MAX_SPEED - abs(self.velocity[1])
            if self.velocity[0] < 0:
                dx = -dx
            if self.velocity[1] < 0:
                dy = -dy
            self.apply_force((dx, dy))

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()

class AvoidWall(Game):
    def init_game(self):
        super().init_game()
        self.particles = [Avoider(WIDTH // 2, HEIGHT // 2) for _ in range(PARTICLE_COUNT)]

    def update_game(self):
        super().update_game()
        self.particles = [p for p in self.particles if p.is_alive_after_update(self.dt)]
        return True

    def draw_game(self):
        self.screen.fill(BLACK)
        for particle in self.particles:
            particle.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = AvoidWall("Avoid Wall", size=(WIDTH, HEIGHT))
    game.run()
