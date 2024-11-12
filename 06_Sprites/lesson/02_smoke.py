import pygame
from game import Game
from delta_time_particle import DeltaTimeParticle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FADE_OUT_SPEED = 300
CREATION_RATE = 50


class SmokeParticle(DeltaTimeParticle):

    def __init__(self, x, y):
        super().__init__(x, y)
        surface = pygame.image.load("fading_circle.png")
        surface = pygame.transform.scale(surface, (50, 50))
        self.set_surface(surface.convert_alpha())
        self.set_fade_speed(FADE_OUT_SPEED)

    def update(self, dt=1):
        if not super().update(dt):
            return False
        if not self.fade(dt):
            return False
        if self.position[1] < 0:
            return False
        return True



class SmokingCursor(Game):
    def init_game_state(self):
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
        self.particles = [particle for particle in self.particles if particle.update(self.dt)]
        return True

    def draw_game(self):
        self.screen.fill(BLACK)
        for particle in self.particles:
            particle.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = SmokingCursor("Smoking Cursor")
    game.run()
