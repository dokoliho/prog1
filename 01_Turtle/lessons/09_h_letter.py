from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.hideturtle()
    draw_h(sophia)
    sophia.screen.mainloop()

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


main()