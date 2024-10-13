# Zeichnen der Flagge Deutschlands mit der Turtle

from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.pencolor('Black')
    sophia.fillcolor('Black')
    draw_rectangle(sophia,200, 50)
    next_shape(sophia)
    sophia.pencolor('Red')
    sophia.fillcolor('Red')
    draw_rectangle(sophia, 200,50)
    next_shape(sophia)
    sophia.pencolor('Yellow')
    sophia.fillcolor('Yellow')
    draw_rectangle(sophia, 200,50)
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_rectangle(turtle, width, height):
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.end_fill()

def next_shape(turtle):
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()

main()
