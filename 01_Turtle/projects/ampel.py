# Zeichnen einer Ampel

from turtle import Turtle

def main():
    zoe = Turtle()
    draw_traffic_light(zoe)
    zoe.hideturtle()
    zoe.screen.mainloop()


def draw_traffic_light(t):
    draw_case(t)
    t.forward(35)
    t.left(90)
    t.forward(10)
    draw_light(t, 'green')
    t.forward(60)
    draw_light(t, 'yellow')
    t.forward(60)
    draw_light(t, 'red')


def draw_case(t):
    t.pencolor('black')
    t.fillcolor('black')
    t.pendown()
    t.begin_fill()
    draw_rectangle(t, 70, 190)
    t.end_fill()
    t.penup()


def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def draw_light(t, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.circle(25)
    t.end_fill()
    t.penup()
    t.left(90)

main()