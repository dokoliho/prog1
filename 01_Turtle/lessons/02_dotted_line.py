# Sophia zeichnet eine gestrichelte Linie

from turtle import Turtle

sophia = Turtle()
sophia.hideturtle()

for _ in range(10):
    sophia.penup()
    sophia.forward(5)
    sophia.pendown()
    sophia.forward(5)

sophia.screen.mainloop()
