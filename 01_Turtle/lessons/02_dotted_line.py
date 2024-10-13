# Sophia zeichnet eine gestrichelte Linie

from turtle import Turtle

sophia = Turtle()

def main():
    sophia.shape('turtle')
    draw_dotted_line()
    sophia.screen.mainloop()

def draw_dotted_line():
    for _ in range(10):
        sophia.penup()
        sophia.forward(5)
        sophia.pendown()
        sophia.forward(5)

main()

