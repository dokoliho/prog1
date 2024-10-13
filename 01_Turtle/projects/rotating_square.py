from turtle import Turtle

def main():
    sophia = Turtle()
    draw_mandala(sophia, 100)
    sophia.screen.mainloop()

def draw_mandala(turtle, length):
    for _ in range(18):
        draw_square(turtle, length)
        turtle.right(20)

def draw_square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


main()