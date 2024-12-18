import pygame
from game import Game
from delta_time_particle import DeltaTimeParticle
from image_particle import ImageParticle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FADE_OUT_SPEED = -200
CREATION_RATE = 50


class SmokeParticle(ImageParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_target_size((50, 50))
        self.read_image("fading_circle.png")
        self.set_fade_speed(FADE_OUT_SPEED)

    def is_alive_after_update(self, dt):
        self.update(dt)
        return self.is_visible()



class SmokingCursor(Game):
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
        return True

    def spawn_floating_particle(self):
        init_pos = pygame.mouse.get_pos()
        particle = SmokeParticle(init_pos[0], init_pos[1])
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
    game = SmokingCursor("Smoking Cursor")
    game.run()
