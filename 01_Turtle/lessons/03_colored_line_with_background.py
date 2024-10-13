# Sophia zeichnet eine farbige Linie mit Hintergrund

from turtle import Turtle

sophia = Turtle()

def main():
    sophia.hideturtle()
    sophia.pensize(5)
    sophia.screen.bgcolor('yellow')
    sophia.back(100)
    draw_colored_line()
    sophia.screen.mainloop()

def draw_colored_line():
    sophia.pencolor('green')
    sophia.forward(30)
    sophia.pencolor('blue')
    sophia.forward(30)
    sophia.pencolor('red')
    sophia.forward(30)
    sophia.pencolor('white')
    sophia.forward(30)
    sophia.pencolor('black')
    sophia.forward(30)
    sophia.pencolor('#c72426')
    sophia.forward(30)

main()

