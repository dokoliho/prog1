# Description: Fireworks animation
import pygame
import random
import math
from game import Game
from delta_time_particle import DeltaTimeParticle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FLOATING_SPEED = -100
FADE_OUT_SPEED = -200
CREATION_RATE = 80
EXPLOSION_COUNT = 1000
MIN_LIFETIME = 1000
MAX_LIFETIME = 1200
MIN_EXPLOSION_SPEED = 50
MAX_EXPLOSION_SPEED = 400

class FloatingParticle(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        surface = pygame.Surface((2, 2))
        surface.fill(BLACK)
        surface.set_colorkey(BLACK)
        pygame.draw.circle(surface, WHITE, (1, 1), 1)
        self.set_surface(surface.convert_alpha())
        self.velocity = (0, FLOATING_SPEED)
        self.set_fade_speed(FADE_OUT_SPEED)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible() and self.position[1] > 0


class ExplodingParticle(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.creation_time = pygame.time.get_ticks()
        self.lifetime = random.randint(MIN_LIFETIME, MAX_LIFETIME)
        self.color = random.choice([RED, GREEN, BLUE])
        surface = pygame.Surface((4, 4))
        surface.fill(BLACK)
        surface.set_colorkey(BLACK)
        pygame.draw.circle(surface, self.color, (2, 2), 2)
        self.set_surface(surface.convert_alpha())
        direction = math.radians(random.randint(0, 360))
        speed = random.randint(MIN_EXPLOSION_SPEED, MAX_EXPLOSION_SPEED)
        self.velocity = (math.cos(direction) * speed, math.sin(direction) * speed)
        self.set_fade_speed(FADE_OUT_SPEED)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()

class Firework(Game):
    def init_game(self):
        super().init_game()
        self.particles = []
        self.floating_timer = pygame.event.custom_type()
        pygame.time.set_timer(self.floating_timer, 1000 // CREATION_RATE)

    def handle_event(self, event):
        if not super().handle_event(event):
            return False
        if event.type == self.floating_timer:
            self.spawn_floating_particle()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.spawn_exploding_particle(EXPLOSION_COUNT)
        return True

    def spawn_floating_particle(self):
        init_pos = pygame.mouse.get_pos()
        particle = FloatingParticle(init_pos[0] + random.randint(-10, 10), init_pos[1] + random.randint(-10, 10))
        self.particles.append(particle)

    def spawn_exploding_particle(self, count):
        pos = pygame.mouse.get_pos()
        for _ in range(count):
            particle = ExplodingParticle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            self.particles.append(particle)

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
    game = Firework("Feuerwerk")
    game.run()
