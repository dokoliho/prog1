from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.screen.bgcolor('blue')
    draw_building(sophia)
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_building(turtle):
    turtle.fillcolor('black')
    turtle.pencolor('black')
    draw_filled_rectangle(turtle,100, 210)
    turtle.left(90)
    for _ in range(5):
        draw_floor(turtle)

def draw_floor(turtle):
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    for _ in range(3):
        draw_window(turtle)
        next_window(turtle)
    turtle.penup()
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(30)

def draw_window(turtle):
    turtle.fillcolor('yellow')
    turtle.pencolor('yellow')
    draw_filled_rectangle(turtle, 20, 30)

def next_window(turtle):
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

def draw_filled_rectangle(turtle, width, height):
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

main()