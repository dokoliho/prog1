# Zeichnen eines gefüllten Quadrats mit der Turtle
from turtle import Turtle

def main():
    sophia = Turtle()
    sophia.fillcolor('red')
    draw_filled_square(sophia, 100)
    sophia.screen.mainloop()

# Eine Turtle zeichnet ein gefülltes Quadrat
def draw_filled_square(t, length):
    t.begin_fill()
    draw_square(t, length)
    t.end_fill()

# Eine Turtle zeichnet ein Quadrat
def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

main()