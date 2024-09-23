from turtle import Turtle

sophia = Turtle()

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

draw_h(sophia)

sophia.screen.mainloop()
