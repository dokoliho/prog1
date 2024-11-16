import pygame
from delta_time_particle import DeltaTimeParticle

class ImageParticle(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._image = None
        self._target_size = None

    def set_target_size(self, target_size):
        self._target_size = target_size

    def read_image(self, image_name):
        image = pygame.image.load(image_name)
        color = image.get_at((0, 0))
        image.set_colorkey(color)
        if self._target_size != None:
            image = pygame.transform.scale(image, self._target_size)
        self._image = image.convert_alpha()

    def draw(self, screen):
        if self._image is None:
            return
        self._image.set_alpha(self._alpha)
        blit_position = (self.position[0] - self._image.get_width() / 2,
                         self.position[1] - self._image.get_height() / 2)
        screen.blit(self._image, blit_position)

    def is_visible(self):
        return super().is_visible() and self._image != None
