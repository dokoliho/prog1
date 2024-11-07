import pygame

class Particle:
    def __init__(self, x, y):
        self.position = (x, y)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self._surface = None

    def set_surface(self, surface):
        self._surface = surface

    def apply_force(self, force):
        self.acceleration = (self.acceleration[0] + force[0], self.acceleration[1] + force[1])

    def update(self):
        self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.acceleration = (0, 0)

    def draw(self, screen):
        if self._surface is not None:
            blit_positon = (self.position[0] - self._surface.get_width()/2,
                            self.position[1] - self._surface.get_height()/2)
            screen.blit(self._surface, blit_positon)


if __name__ == "__main__":
    player = Particle(0, 0)
    player.apply_force((2, 1))
    for _ in range(3):
        player.update()
        print(player.position)