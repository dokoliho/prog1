from turtle import Turtle

def main():
    sophia = Turtle()
    draw_archery_target(sophia)
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_archery_target(turtle):
    draw_circle(turtle, 90, 'red')
    draw_circle(turtle, 60, 'white')
    draw_circle(turtle, 30, 'red')


def draw_circle(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)

main()