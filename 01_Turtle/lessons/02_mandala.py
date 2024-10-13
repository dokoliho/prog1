from turtle import Turtle

sophia = Turtle()

def main():
    sophia.hideturtle()
    draw_mandala()
    sophia.screen.mainloop()

def draw_mandala():
    for _ in range(18):
        draw_square()
        sophia.right(20)

def draw_square():
    for _ in range(4):
        sophia.forward(100)
        sophia.right(90)

main()
