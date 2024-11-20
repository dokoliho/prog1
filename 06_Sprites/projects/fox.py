import pygame
from game import Game
from sprite import Sprite

BLACK = (0, 0, 0)
SPEED = 50

class FoxSprite(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_target_size((64, 64))
        self.read_sprite_sheet("fox.png", 4, 4)
        self.add_animation("standing", [1])
        self.add_animation("moving_left", [4, 5, 6, 7])
        self.add_animation("moving_right", [8, 9, 10, 11])
        self.add_animation("moving_up", [12, 13, 14, 15])
        self.add_animation("moving_down", [0, 1, 2, 3])

    def update(self, dt=1):
        super().update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity = (0, -SPEED)
            self.set_repeat_animation("moving_up", 10)
        elif keys[pygame.K_DOWN]:
            self.velocity = (0, SPEED)
            self.set_repeat_animation("moving_down", 10)
        elif keys[pygame.K_LEFT]:
            self.velocity = (-SPEED, 0)
            self.set_repeat_animation("moving_left", 10)
        elif keys[pygame.K_RIGHT]:
            self.velocity = (SPEED, 0)
            self.set_repeat_animation("moving_right", 10)
        else:
            self.velocity = (0, 0)
            self.set_repeat_animation("standing", 2)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()


class FoxGame(Game):
    def init_game(self):
        super().init_game()
        width, height = self.size
        self.fox = FoxSprite(width // 2, height // 2)
        self.fox.set_repeat_animation("standing", 2)

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
    game = FoxGame("Running Fox")
    game.run()
