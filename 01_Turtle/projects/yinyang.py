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
    sophia.right(90)
    sophia.forward(radius)
    sophia.left(90)
    draw_fish_shape(sophia, radius)

    # Weiße Hälfte
    zoe.penup()
    zoe.left(90)
    zoe.forward(radius)
    zoe.left(90)
    draw_fish_shape(zoe, radius)

    # Schwarzer Punkt
    draw_dot(sophia, radius)

    # Weißer Punkt
    draw_dot(zoe, radius)

def draw_fish_shape(t, radius):
    t.pendown()
    t.begin_fill()
    t.circle(radius, 180)  # Halbkreis
    t.circle(radius // 2, 180)
    t.circle(-radius // 2, 180)
    t.end_fill()

def draw_dot(t, radius):
    t.penup()
    t.right(90)
    t.forward(radius//2 - radius//10)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.circle(radius // 10)
    t.end_fill()


main()