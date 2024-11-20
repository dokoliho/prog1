import pygame

class Particle:
    def __init__(self, x, y):
        self.position = (x, y)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self._fade_speed = 0
        self._alpha = 255
        self._surface = None

    def set_surface(self, surface):
        self._surface = surface

    def set_fade_speed(self, fade_speed):
        self._fade_speed = fade_speed

    def apply_force(self, force):
        self.acceleration = (self.acceleration[0] + force[0], self.acceleration[1] + force[1])

    def update(self, dt=1):
        self.velocity = (self.velocity[0] + self.acceleration[0] * dt, self.velocity[1] + self.acceleration[1] * dt)
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)
        self.acceleration = (0, 0)
        return True

    def fade(self, dt):
        self._alpha -= self._fade_speed * dt
        if self._alpha <= 0:
            return False
        if self._surface != None:
            self._surface.set_alpha(self._alpha)
        return True

    def draw(self, screen):
        if self._surface is not None:
            blit_position = (self.position[0] - self._surface.get_width()/2,
                             self.position[1] - self._surface.get_height()/2)
            screen.blit(self._surface, blit_position)


if __name__ == "__main__":
    player = Particle(0, 0)
    player.apply_force((2, 1))
    for _ in range(3):
        player.update()
        print(player.position)