# Zeichnet ein Mandala mit der Turtle-Grafik

from turtle import Turtle

sophia = Turtle()
sophia.speed(0)

for _ in range(36):
    sophia.pencolor("Blue")
    sophia.circle(100)
    sophia.pencolor("Red")
    sophia.forward(200)
    sophia.left(120)
    sophia.color("Orange")
    sophia.forward(100)
    sophia.left(70)
    sophia.forward(15)

sophia.screen.mainloop()

