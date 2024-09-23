from turtle import Turtle


def draw_archery_target(turtle):
    draw_circle(turtle, 30, 'red')
    draw_circle(turtle, 20, 'white')
    draw_circle(turtle, 10, 'red')


def draw_circle(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)


sophia = Turtle()
draw_archery_target(sophia)
sophia.hideturtle()
sophia.screen.mainloop()