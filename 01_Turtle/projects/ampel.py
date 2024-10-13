# Zeichnen einer Ampel

from turtle import Turtle

def main():
    zoe = Turtle()
    draw_traffic_light(zoe)
    zoe.hideturtle()
    zoe.screen.mainloop()


def draw_traffic_light(turtle):
    draw_case(turtle)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(10)
    draw_light(turtle, 'green')
    turtle.forward(60)
    draw_light(turtle, 'yellow')
    turtle.forward(60)
    draw_light(turtle, 'red')


def draw_case(turtle):
    turtle.pencolor('black')
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.begin_fill()
    draw_rectangle(turtle, 70, 190)
    turtle.end_fill()
    turtle.penup()


def draw_rectangle(turtle, width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def draw_light(turtle, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(90)
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)

main()