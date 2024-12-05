import pygame
import random

from pygame.examples.moveit import HEIGHT

from game import Game
from image_particle import ImageParticle
from delta_time_particle import DeltaTimeParticle

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
SHIP_SPEED = 200
BULLET_RADIUS = 2
BULLET_SPEED = -400


class Spaceship(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_target_size((74, 59))
        self.read_image("spaceship.png")
        self.position = (x, y-self._image.get_height() // 2)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()



class Bullet(DeltaTimeParticle):
        def __init__(self, x, y):
            super().__init__(x, y)
            surface = pygame.Surface((BULLET_RADIUS*2, BULLET_RADIUS*2))
            surface.fill(BLACK)
            surface.set_colorkey(BLACK)
            pygame.draw.circle(surface, YELLOW, (BULLET_RADIUS, BULLET_RADIUS), BULLET_RADIUS)
            self.set_surface(surface.convert_alpha())
            self.velocity = (0, BULLET_SPEED)

        def is_alive_after_update(self, dt):
            self.update(dt)
            return self.is_visible() and self.position[1] > 0



class SpaceShip(Game):
    def init_game(self):
        super().init_game()
        width, height = self.size
        self.ship = Spaceship(width // 2, height)
        self.bullets = []

    def handle_event(self, event):
        if not super().handle_event(event):
            return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet = Bullet(self.ship.position[0], self.ship.position[1])
            self.bullets.append(bullet)
        if keys[pygame.K_LEFT]:
            self.ship.velocity = (-SHIP_SPEED, 0)
        elif keys[pygame.K_RIGHT]:
            self.ship.velocity = (SHIP_SPEED, 0)
        else:
            self.ship.velocity = (0, 0)
        return True

    def update_game(self):
        super().update_game()
        self.ship.update(self.dt)
        self.bullets = [b for b in self.bullets if b.is_alive_after_update(self.dt)]
        return True


    def draw_game(self):
        self.screen.fill(BLUE)
        self.ship.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = SpaceShip("Shooting Spaceship", size=SIZE)
    game.run()