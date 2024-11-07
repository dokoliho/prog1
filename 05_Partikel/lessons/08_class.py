class Particle:

    def __init__(self, x=0, y=0):
        self.position = (x, y)


player = Particle(50, 50)
print(player.position)



