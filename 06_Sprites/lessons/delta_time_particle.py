from particle import Particle

class DeltaTimeParticle(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._fade_speed = 0
        self._alpha = 255

    def set_fade_speed(self, fade_speed):
        self._fade_speed = fade_speed

    def set_alpha(self, alpha):
        self._alpha = alpha

    def update(self, dt=1):
        self.velocity = (self.velocity[0] + self.acceleration[0] * dt, self.velocity[1] + self.acceleration[1] * dt)
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)
        self.acceleration = (0, 0)
        self.fade(dt)

    def fade(self, dt):
        self._alpha += self._fade_speed * dt
        self._alpha = max(0, min(self._alpha, 255))
        if self._surface != None:
            self._surface.set_alpha(self._alpha)

    def is_visible(self):
        return self._alpha > 0

