from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.pencolor('red')
    sophia.fillcolor('red')
    draw_segment(sophia, 240, 100)
    sophia.pencolor('blue')
    sophia.fillcolor('blue')
    draw_segment(sophia,90, 100)
    sophia.pencolor('green')
    sophia.fillcolor('green')
    draw_segment(sophia, 30, 100)
    sophia.hideturtle()
    sophia.screen.mainloop()

def draw_segment(turtle, degree, length):
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(length, degree)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(degree)
    turtle.backward(length)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(length)
    turtle.left(degree)
    turtle.backward(length)
    turtle.right(90)

main()