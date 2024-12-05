import pygame
import random

from pygame.examples.moveit import HEIGHT

from game import Game
from image_particle import ImageParticle
from delta_time_particle import DeltaTimeParticle

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
SHIP_SPEED = 200
BULLET_RADIUS = 2
BULLET_SPEED = -400
BOMB_RADIUS = 5
BOMB_SPEED = 100
BOMB_DROP_RATE = 0.2 # per Second


class Spaceship(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.alive = True
        self.set_target_size((74, 59))
        self.read_image("spaceship.png")
        self.position = (x, y-self._image.get_height() // 2)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()


class Ufo(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = (100, 0)
        self.set_target_size((77, 32))
        self.alive = True
        self.read_image("ufo.png")
        self._time_since_last_drop = random.random() / BOMB_DROP_RATE

    def set_game(self, game):
        self._game = game

    def update(self, dt=1):
        super().update(dt)
        if self.position[0] < 0 or self.position[0] > self._game.size[0]:
            self.velocity = (-self.velocity[0], self.velocity[1])
        self._time_since_last_drop += dt
        time_between_drops = 1 / BOMB_DROP_RATE
        if self._time_since_last_drop > time_between_drops:
            self._time_since_last_drop -= time_between_drops
            bomb = Bomb(self.position[0], self.position[1])
            self._game.bombs.append(bomb)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible() and self.alive


class Bullet(DeltaTimeParticle):
        def __init__(self, x, y):
            super().__init__(x, y)
            surface = pygame.Surface((BULLET_RADIUS*2, BULLET_RADIUS*2))
            surface.fill(BLUE)
            surface.set_colorkey(BLUE)
            pygame.draw.circle(surface, YELLOW, (BULLET_RADIUS, BULLET_RADIUS), BULLET_RADIUS)
            self.set_surface(surface.convert_alpha())
            self.velocity = (0, BULLET_SPEED)

        def is_alive_after_update(self, dt, ufos):
            self.update(dt)
            rect1 = pygame.Rect(0, 0, self._surface.get_width(), self._surface.get_height())
            rect1.center = self.position
            for ufo in ufos:
                rect2 = pygame.Rect(0, 0, ufo._image.get_width(), ufo._image.get_height())
                rect2.center = ufo.position
                if rect1.colliderect(rect2):
                    ufo.alive = False
                    return False
            return self.is_visible() and self.position[1] > 0


class Bomb(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        surface = pygame.Surface((BOMB_RADIUS * 2, BOMB_RADIUS * 2))
        surface.fill(BLUE)
        surface.set_colorkey(BLUE)
        pygame.draw.circle(surface, RED, (BOMB_RADIUS, BOMB_RADIUS), BOMB_RADIUS)
        self.set_surface(surface.convert_alpha())
        self.velocity = (0, BOMB_SPEED)

    def is_alive_after_update(self, dt, ship):
        self.update(dt)
        rect1 = pygame.Rect(0, 0, self._surface.get_width(), self._surface.get_height())
        rect1.center = self.position
        rect2 = pygame.Rect(0, 0, ship._image.get_width(), ship._image.get_height())
        rect2.center = ship.position
        if rect1.colliderect(rect2):
            ship.alive = False
            return False
        return self.is_visible() and self.position[1] < HEIGHT


class SpaceInvaders(Game):
    def init_game(self):
        super().init_game()
        width, height = self.size
        self.ship = Spaceship(width // 2, height)
        self.bullets = []
        self.bombs = []
        self.ufos = [ Ufo(x, 100) for x in range(50, width, 100) ]
        for ufo in self.ufos:
            ufo.set_game(self)

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
        self.bullets = [b for b in self.bullets if b.is_alive_after_update(self.dt, self.ufos)]
        self.bombs = [b for b in self.bombs if b.is_alive_after_update(self.dt, self.ship)]
        self.ufos = [u for u in self.ufos if u.is_alive_after_update(self.dt)]
        return self.ship.alive


    def draw_game(self):
        self.screen.fill(BLUE)
        self.ship.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for bomb in self.bombs:
            bomb.draw(self.screen)
        for ufo in self.ufos:
            ufo.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = SpaceInvaders("Space Invaders", size=SIZE)
    game.run()