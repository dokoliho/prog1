from turtle import Turtle

from turtle import Turtle


def main():
    sophia = Turtle()
    sophia.speed(1)
    sophia.screen.bgcolor("white")

    draw_pie_chart(sophia)

    sophia.hideturtle()
    sophia.screen.mainloop()


def draw_pie_chart(turtle):
    draw_segment(turtle, 240, 'red')  # Sophia 240 Grad
    draw_segment(turtle, 90, 'blue')  # Zoe 90 Grad
    draw_segment(turtle, 30, 'green')  # Reeborg 30 Grad


def draw_segment(turtle, angle, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(100, angle)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.left(180)

main()


