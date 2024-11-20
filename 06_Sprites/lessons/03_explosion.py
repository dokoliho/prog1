import pygame
from game import Game
from sprite import Sprite

BLACK = (0, 0, 0)

class ExplosionSprite(Sprite):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_target_size((64, 64))
        self.read_sprite_sheet("explosion.png", 6, 8, sprite_height=256)
        self.add_animation("explode", list(range(6*8)))

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()



class ExplosionGame(Game):

    def init_game(self):
        super().init_game()
        self.sprites = []

    def handle_event(self, event):
        if not super().handle_event(event):
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            explosion = ExplosionSprite(x, y)
            explosion.set_single_animation("explode", 30)
            self.sprites.append(explosion)
        return True

    def update_game(self):
        super().update_game()
        self.sprites = [s for s in self.sprites if s.is_alive_after_update(self.dt)]
        return True

    def draw_game(self):
        self.screen.fill(BLACK)
        for sprite in self.sprites:
            sprite.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = ExplosionGame("Explosion")
    game.run()