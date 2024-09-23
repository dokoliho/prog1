# Zeichnen des Wortes "Hello" mit der Turtle

from turtle import Turtle

def space(turtle):
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

def draw_h(turtle):
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(90)

def draw_e(turtle):
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

def draw_l(turtle):
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)

def draw_o(turtle):
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()

sophia = Turtle()
sophia.speed(0)
draw_h(sophia)
space(sophia)
draw_e(sophia)
space(sophia)
draw_l(sophia)
space(sophia)
draw_l(sophia)
space(sophia)
draw_o(sophia)


sophia.screen.mainloop()