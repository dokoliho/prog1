from particle import Particle

class DeltaTimeParticle(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.fade_speed = 0
        self.alpha = 255

    def set_fade_speed(self, fade_speed):
        self.fade_speed = fade_speed

    def set_alpha(self, alpha):
        self.alpha = alpha

    def update(self, dt=1):
        self.velocity = (self.velocity[0] + self.acceleration[0] * dt, self.velocity[1] + self.acceleration[1] * dt)
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)
        self.acceleration = (0, 0)
        return True

    def fade(self, dt):
        self.alpha -= self.fade_speed * dt
        if self.alpha <= 0:
            return False
        if self._surface != None:
            self._surface.set_alpha(self.alpha)
        return True



