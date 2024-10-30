from turtle import Turtle

def main():
    sophia = Turtle()
    zoe = Turtle()
    sophia.screen.bgcolor('grey')
    sophia.pencolor('black')
    sophia.fillcolor('black')
    zoe.pencolor('white')
    zoe.fillcolor('white')

    draw_yin_yang(sophia, zoe, radius=100)

    sophia.hideturtle()
    zoe.hideturtle()
    sophia.screen.mainloop()


def draw_yin_yang(sophia, zoe, radius):
    # Schwarze Hälfte
    sophia.penup()
    sophia.goto(0, -radius)
    sophia.pendown()
    sophia.begin_fill()
    sophia.circle(radius, 180)  # Halbkreis
    sophia.circle(radius // 2, 180)
    sophia.circle(-radius // 2, 180)
    sophia.end_fill()

    # Weiße Hälfte
    zoe.penup()
    zoe.goto(0, -radius)
    zoe.left(180)
    zoe.pendown()
    zoe.begin_fill()
    zoe.circle(-radius, 180)  # Halbkreis
    zoe.left(180)
    zoe.circle(radius // 2, 180)
    zoe.circle(-radius // 2, 180)
    zoe.end_fill()

    # Schwarzer Punkt
    sophia.penup()
    sophia.goto(0, -((radius // 2) - (radius // 10)))
    sophia.pendown()
    sophia.begin_fill()
    sophia.circle(radius // 10)
    sophia.end_fill()

    # Weißer Punkt
    zoe.penup()
    zoe.goto(0, (radius // 2) + (radius // 10))
    zoe.pendown()
    zoe.begin_fill()
    zoe.circle(radius // 10)
    zoe.end_fill()




main()