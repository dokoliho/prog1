# Zeichnen von Flaggen mit der Turtle
from turtle import Turtle

def main():
    Turtle.draw_flag = draw_flag
    sophia = Turtle()
    sophia.draw_flag('green', 'white', 'red')
    sophia.backward(600)
    sophia.right(90)
    sophia.forward(400)
    sophia.left(90)
    sophia.draw_flag('blue', 'white', 'red')
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_flag(turtle, color1, color2, color3):
    turtle.pencolor('black')
    turtle.pendown()
    draw_rectangle(turtle, 600, 300)
    turtle.penup()
    draw_segment(turtle, color1)
    draw_segment(turtle, color2)
    draw_segment(turtle, color3)

def draw_segment(turtle, color):
    turtle.fillcolor(color)
    draw_filled_rectangle(turtle, 200, 300)
    turtle.forward(200)

def draw_filled_rectangle(turtle, width, height):
    turtle.begin_fill()
    draw_rectangle(turtle, width, height)
    turtle.end_fill()

def draw_rectangle(turtle, width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


main()
