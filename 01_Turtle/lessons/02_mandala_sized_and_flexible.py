from turtle import Turtle

zoe = Turtle()

def main():
    zoe.hideturtle()
    draw_mandala(zoe, 60)
    zoe.screen.mainloop()

def draw_mandala(turtle, size):
    for _ in range(18):
        draw_square(turtle, size)
        turtle.right(20)

def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

main()
