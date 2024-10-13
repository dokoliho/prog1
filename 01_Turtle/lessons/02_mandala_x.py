from turtle import Turtle

zoe = Turtle()

def main():
    zoe.hideturtle()
    zoe.speed(0)
    draw_mandala(zoe, 60)
    zoe.screen.mainloop()

def draw_mandala(turtle, size):
    for _ in range(6):
        turtle.pencolor('red')
        draw_triangle(turtle, size)
        turtle.right(30)
        turtle.pencolor('blue')
        draw_triangle(turtle, size)
        turtle.right(30)


def draw_triangle(turtle, size):
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)

main()
