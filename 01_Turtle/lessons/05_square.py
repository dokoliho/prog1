# Zeichnen eines Quadrats mit der Turtle
from turtle import Turtle

sophia = Turtle()

# Sophia zeichnet ein Quadrat
def draw_square():
    for _ in range(4):
        sophia.forward(100)
        sophia.right(90)

draw_square()

sophia.screen.mainloop()