from turtle import Turtle

sophia = Turtle()

def main():
    sophia.hideturtle()
    draw_mandala()
    sophia.screen.mainloop()

def draw_mandala(size=100):
    for _ in range(18):
        draw_square(size)
        sophia.right(20)

def draw_square(size):
    for _ in range(4):
        sophia.forward(size)
        sophia.right(90)

main()
