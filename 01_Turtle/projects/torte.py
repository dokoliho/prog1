from turtle import Turtle

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


Turtle.draw_segment = draw_segment
sophia = Turtle()
sophia.pencolor('red')
sophia.fillcolor('red')
sophia.draw_segment(240, 100)
sophia.pencolor('blue')
sophia.fillcolor('blue')
sophia.draw_segment(90, 100)
sophia.pencolor('green')
sophia.fillcolor('green')
sophia.draw_segment(30, 100)
sophia.hideturtle()
sophia.screen.mainloop()
