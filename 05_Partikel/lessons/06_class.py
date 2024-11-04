class Particle:

    def set_position(self, x, y):
        self.position = (x, y)


player = Particle()
player.set_position(0, 0)
print(player.position)
