import pygame
import random

from game import Game
from image_particle import ImageParticle
from delta_time_particle import DeltaTimeParticle
from sprite import Sprite

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SHIP_SPEED = 200
SHIP_IMAGE = "spaceship.png"
SHIP_SIZE = (58, 66)
BULLET_RADIUS = 2
BULLET_SPEED = -400
BOMB_RADIUS = 5
BOMB_SPEED = 100
BOMB_DROP_RATE = 0.2 # per Second
BONUS_SPEED = -100
BONUS_FADE = -200
UFO_IMAGE = "ufo.png"
UFO_SIZE = (77, 32)
UFO_START_SPEED = 100

class Spaceship(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.alive = True
        self.set_target_size(SHIP_SIZE)
        self.read_image(SHIP_IMAGE)
        self.position = (x, y-self._image.get_height() // 2)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()


class Ufo(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = (100, 0)
        self.set_target_size(UFO_SIZE)
        self.alive = True
        self.read_image(UFO_IMAGE)
        self._time_since_last_drop = random.random() / BOMB_DROP_RATE
        self.drop_rate = BOMB_DROP_RATE

    def update(self, dt, game):
        super().update(dt)
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.velocity = (-self.velocity[0], self.velocity[1])
        self._time_since_last_drop += dt
        time_between_drops = 1 / self.drop_rate
        if self._time_since_last_drop > time_between_drops:
            self._time_since_last_drop -= time_between_drops
            bomb = Bomb(self.position[0], self.position[1])
            game.bombs.append(bomb)

    def is_alive_after_update(self, dt, game):
        self.update(dt, game)
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
                if rect1.colliderect(rect2) and ufo.alive:
                    ufo.alive = False
                    game.bonus_particles.append(Bonus(ufo.position[0], ufo.position[1]))
                    game.score += 100
                    print(game.score)
                    explosion = ExplosionSprite(ufo.position[0], ufo.position[1])
                    explosion.set_single_animation("explode", 30)
                    game.explosions.append(explosion)
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

    def is_alive_after_update(self, dt, game):
        self.update(dt)
        ship = game.ship
        if ship.alive:
            rect1 = pygame.Rect(0, 0, self._surface.get_width(), self._surface.get_height())
            rect1.center = self.position
            rect2 = pygame.Rect(0, 0, ship._image.get_width(), ship._image.get_height())
            rect2.center = ship.position
            if rect1.colliderect(rect2):
                ship.alive = False
                explosion = ExplosionSprite(ship.position[0], ship.position[1])
                explosion.set_single_animation("explode", 30)
                game.explosions.append(explosion)
                return False
        return self.is_visible() and self.position[1] < HEIGHT


class Bonus(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        font = pygame.font.Font(None, 20)
        surface = font.render("100", True, WHITE)
        self.set_surface(surface.convert_alpha())
        self.velocity = (0, BONUS_SPEED)
        self.set_fade_speed(BONUS_FADE)

    def is_alive_after_update(self, dt, game):
        self.update(dt)
        return self.is_visible() and self.position[1] > 0


class ExplosionSprite(Sprite):
    target_size = (64, 64)
    images = []

    @staticmethod
    def prepare_sprite_sheet():
        ExplosionSprite.images = (
            Sprite.load_sprite_sheet(  "explosion.png",6, 8,
                                        sprite_height=256, target_size=ExplosionSprite.target_size))

    def __init__(self, x, y):
        super().__init__(x, y)
        self._images = ExplosionSprite.images
        self.add_animation("explode", list(range(6*8)))

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()


class SpaceInvaders(Game):
    def init_game(self):
        super().init_game()
        ExplosionSprite.prepare_sprite_sheet()
        width, height = self.size
        self.ship = Spaceship(width // 2, height)
        self.bullets = []
        self.bombs = []
        self.explosions = []
        self.bonus_particles = []
        self.ufo_speed = UFO_START_SPEED
        self.bomb_drop_rate = BOMB_DROP_RATE
        self.create_ufos()
        self.score = 0
        self.lifes = 3
        image = ImageParticle.load_image(SHIP_IMAGE)
        image = pygame.transform.scale(image, (SHIP_SIZE[0] // 2, SHIP_SIZE[1] // 2))
        self._image = image.convert_alpha()

    def create_ufos(self):
        self.ufos = [ Ufo(x, 100) for x in range(50, WIDTH, 100) ]
        for ufo in self.ufos:
            ufo.velocity = (self.ufo_speed, 0)
            ufo.drop_rate = self.bomb_drop_rate

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
        self.bonus_particles = [b for b in self.bonus_particles if b.is_alive_after_update(self.dt, self)]
        self.bullets = [b for b in self.bullets if b.is_alive_after_update(self.dt, self)]
        self.bombs = [b for b in self.bombs if b.is_alive_after_update(self.dt, self)]
        self.ufos = [u for u in self.ufos if u.is_alive_after_update(self.dt, self)]
        self.explosions = [e for e in self.explosions if e.is_alive_after_update(self.dt)]
        if not self.ship.alive and self.lifes > 0 and len(self.explosions) == 0:
            self.lifes -= 1
            self.ship.alive = True
            self.ship.position = (WIDTH // 2, HEIGHT - self.ship._image.get_height() // 2)
        if len(self.ufos) == 0:
            self.ufo_speed += 10
            self.bomb_drop_rate += 0.1
            self.create_ufos()
        return True


    def draw_game(self):
        self.screen.fill(BLACK)
        if self.ship.alive:
            self.ship.draw(self.screen)
        elif self.lifes == 0:
            font = pygame.font.Font(None, 72)
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text, text_rect)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for bomb in self.bombs:
            bomb.draw(self.screen)
        for ufo in self.ufos:
            ufo.draw(self.screen)
        for explosion in self.explosions:
            explosion.draw(self.screen)
        for bonus in self.bonus_particles:
            bonus.draw(self.screen)
        for remaing_lifes in range(self.lifes):
            self.screen.blit(self._image, (remaing_lifes * (self._image.get_width()+10) + 10, 10))
        font = pygame.font.Font(None, 32)
        text = font.render(f"{self.score:05}", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH-50, 20))
        self.screen.blit(text, text_rect)
        pygame.display.flip()


if __name__ == "__main__":
    game = SpaceInvaders("Space Invaders", size=SIZE)
    game.run()