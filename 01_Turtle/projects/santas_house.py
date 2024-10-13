import math
from turtle import Turtle

def main():
    sophia = Turtle()
    draw_santas_house(sophia, 200)
    sophia.screen.mainloop()

def draw_santas_house(turtle, length):
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90 + 45)
    turtle.forward(1.4142 * length)
    turtle.left(90 + 45)
    turtle.forward(length)
    turtle.left(90 + 45)
    turtle.forward(1.4142 * length)
    turtle.right(45 + 30)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(30)
    turtle.forward(length)

main()
