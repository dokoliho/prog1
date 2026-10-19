from turtle import Turtle

sophia = Turtle()

def main():
    sophia.hideturtle()
    sophia.speed(0)
    draw_mandala()
    sophia.screen.mainloop()

def draw_mandala():
    for _ in range(9):
        draw_square()
        sophia.right(40)

def draw_square():
    for _ in range(4):
        sophia.forward(100)
        sophia.right(90)

main()
