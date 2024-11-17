class Particle:

    def __init__(self, x=0, y=0):
        self.position = (x, y)

    def __str__(self):
        return f"Particle at {self.position}"


player = Particle(50, 50)
print(player.position)


player = Particle(50, 50)
print(player)

