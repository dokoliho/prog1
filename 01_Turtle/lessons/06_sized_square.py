# Zeichnen eines Quadrats variabler Größe mit der Turtle
from turtle import Turtle

sophia = Turtle()

# Eine Turtle zeichnet ein Quadrat
def draw_square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

draw_square(sophia, 100)

sophia.screen.mainloop()