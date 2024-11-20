import pygame
from delta_time_particle import DeltaTimeParticle

class Sprite(DeltaTimeParticle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._images = []
        self._animations = {}
        self._current_animation = None
        self._time_since_last_frame = 0
        self._target_size = None

    def add_animation(self, animation_name, frame_sequence):
        self._animations[animation_name] = frame_sequence

    def set_target_size(self, target_size):
        self._target_size = target_size

    def read_sprite_sheet(self, sprite_sheet_name,
                          sprite_sheet_rows, sprite_sheet_columns,
                          sprite_width=None, sprite_height=None):
        sprite_sheet = pygame.image.load(sprite_sheet_name)
        if sprite_width == None:
            sprite_width = sprite_sheet.get_width() // sprite_sheet_columns
        if sprite_height == None:
            sprite_height = sprite_sheet.get_height() // sprite_sheet_rows
        for row in range(sprite_sheet_rows):
            for column in range(sprite_sheet_columns):
                rect = pygame.Rect(column * sprite_width, row * sprite_height, sprite_width, sprite_height)
                image = pygame.Surface(rect.size).convert()
                image.blit(sprite_sheet, (0, 0), rect)
                color = image.get_at((0, 0))
                image.set_colorkey(color)
                if self._target_size != None:
                    image = pygame.transform.scale(image, self._target_size)
                self._images.append(image.convert_alpha())
        self._animations["all"] = list(range(len(self._images)))

    def set_single_animation(self, animation_name, fps):
        self._current_animation = (animation_name, fps, 0, False)

    def set_repeat_animation(self, animation_name, fps):
        if self._current_animation != None:
            current_name, current_fps, current_frame, repeated_animation = self._current_animation
            if animation_name == current_name and repeated_animation:
                return
        self._current_animation = (animation_name, fps, 0, True)

    def update(self, dt=1):
        super().update(dt)
        if self._current_animation != None:
            animation_name, fps, current_frame, repeated_animation = self._current_animation
            if animation_name not in self._animations:
                return
            animation_sequence = self._animations[animation_name]
            frame_time = 1 / fps
            self._time_since_last_frame += dt
            if self._time_since_last_frame > frame_time:
                self._time_since_last_frame -= frame_time
                if repeated_animation:
                    current_frame = (current_frame + 1) % len(animation_sequence)
                    self._current_animation = (animation_name, fps, current_frame, True)
                else:
                    current_frame += 1
                    if current_frame >= len(animation_sequence):
                        self._current_animation = None
                    else:
                        self._current_animation = (animation_name, fps, current_frame, False)

    def draw(self, screen):
        if self._current_animation != None:
            animation_name, fps, current_frame, repeated_animation = self._current_animation
            animation_sequence = self._animations[animation_name]
            current_frame = animation_sequence[current_frame]
            surface = self._images[current_frame]
            surface.set_alpha(self._alpha)
            blit_position = (self.position[0] - surface.get_width() / 2,
                             self.position[1] - surface.get_height() / 2)
            screen.blit(surface, blit_position)

    def is_visible(self):
        return super().is_visible() and self._current_animation != None
