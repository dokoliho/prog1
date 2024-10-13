# Zeichnen
from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.screen.bgcolor('Black')
    sophia.pencolor('Red')
    sophia.fillcolor('Red')
    sophia.begin_fill()
    draw_heart(sophia)
    sophia.end_fill()
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_heart(turtle):
    turtle.left(40)
    turtle.forward(178)
    turtle.circle(90,200)
    turtle.right(120)
    turtle.circle(90,200)
    turtle.forward(178)

main()