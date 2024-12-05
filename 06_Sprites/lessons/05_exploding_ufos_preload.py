import pygame
import random

from game import Game
from image_particle import ImageParticle
from delta_time_particle import DeltaTimeParticle
from sprite import Sprite

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
SHIP_SPEED = 200
BULLET_RADIUS = 2
BULLET_SPEED = -400


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

    def update(self, dt=1):
        super().update(dt)
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.velocity = (-self.velocity[0], self.velocity[1])

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

        def is_alive_after_update(self, dt, game):
            self.update(dt)
            rect1 = pygame.Rect(0, 0, self._surface.get_width(), self._surface.get_height())
            rect1.center = self.position
            for ufo in game.ufos:
                rect2 = pygame.Rect(0, 0, ufo._image.get_width(), ufo._image.get_height())
                rect2.center = ufo.position
                if rect1.colliderect(rect2):
                    ufo.alive = False
                    explosion = ExplosionSprite(ufo.position[0], ufo.position[1])
                    explosion.set_single_animation("explode", 30)
                    game.explosions.append(explosion)
                    return False
            return self.is_visible() and self.position[1] > 0


class ExplosionSprite(Sprite):

    target_size = (64, 64)
    images = []

    @staticmethod
    def prepare_sprite_sheet():
        ExplosionSprite.images = Sprite.load_sprite_sheet(  "explosion.png",
                                                          6, 8,
                                                            sprite_height=256,
                                                            target_size=ExplosionSprite.target_size)

    def __init__(self, x, y):
        super().__init__(x, y)
        self._images = ExplosionSprite.images
        self.add_animation("explode", list(range(6*8)))

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()


class ExplodingUfos(Game):
    def init_game(self):
        super().init_game()
        ExplosionSprite.prepare_sprite_sheet()
        width, height = self.size
        self.ship = Spaceship(width // 2, height)
        self.bullets = []
        self.explosions = []
        self.ufos = [ Ufo(x, 100) for x in range(50, width, 100) ]

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
        self.bullets = [b for b in self.bullets if b.is_alive_after_update(self.dt, self)]
        self.explosions = [e for e in self.explosions if e.is_alive_after_update(self.dt)]
        self.ufos = [u for u in self.ufos if u.is_alive_after_update(self.dt)]
        return self.ship.alive


    def draw_game(self):
        self.screen.fill(BLUE)
        self.ship.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for explosion in self.explosions:
            explosion.draw(self.screen)
        for ufo in self.ufos:
            ufo.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = ExplodingUfos("Exploding Ufos", size=SIZE)
    game.run()