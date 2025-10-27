# Eine Turtle erhält eine Methode zum Zeichnen eines gefüllten Quadrats
from turtle import Turtle

def main():
    Turtle.draw_filled_square = draw_filled_square
    sophia = Turtle()
    sophia.fillcolor('red')
    sophia.draw_filled_square(100)
    sophia.screen.mainloop()

# Eine Turtle zeichnet ein Quadrat
def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

# Eine Turtle zeichnet ein gefülltes Quadrat
def draw_filled_square(t, length):
    t.begin_fill()
    draw_square(t, length)
    t.end_fill()

main()
