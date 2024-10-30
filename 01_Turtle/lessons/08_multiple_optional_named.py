

from turtle import Turtle

sophia = Turtle()


def set_colors(pen_color="red", bg_color="blue"):
    sophia.screen.bgcolor(bg_color)
    sophia.pencolor(pen_color)


set_colors(bg_color="green") # Benannter Parameter

sophia.forward(100)

sophia.screen.mainloop()