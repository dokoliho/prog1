# Zeichnen der Flagge Deutschlands mit der Turtle

from turtle import *

def draw_rectangle(width, height):
    begin_fill()
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    end_fill()

def next_shape():
    penup()
    right(90)
    forward(50)
    left(90)
    pendown()

pencolor('Black')
fillcolor('Black')
draw_rectangle(200, 50)
next_shape()
pencolor('Red')
fillcolor('Red')
draw_rectangle(200,50)
next_shape()
pencolor('Yellow')
fillcolor('Yellow')
draw_rectangle(200,50)

done()
