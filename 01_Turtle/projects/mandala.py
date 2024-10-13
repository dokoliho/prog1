# Zeichnet ein Mandala mit der Turtle-Grafik

from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.speed(0)
    draw_mandala(sophia)
    sophia.screen.mainloop()


def draw_mandala(turtle):
    for _ in range(36):
        turtle.pencolor("Blue")
        turtle.circle(100)
        turtle.pencolor("Red")
        turtle.forward(200)
        turtle.left(120)
        turtle.color("Orange")
        turtle.forward(100)
        turtle.left(70)
        turtle.forward(15)


main()
