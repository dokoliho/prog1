from turtle import Turtle
import random

STEPS = 10

def move_drunken(turtle, steps):
    moved = 0
    while moved < steps-STEPS:
        turtle.forward(STEPS)
        angle = random.randint(0, 360)
        turtle.right(angle)
        moved += STEPS
    turtle.forward(steps-moved)

Turtle.stagger = move_drunken

def main():
    random.seed()
    sophia = Turtle()
    sophia.stagger(200)
    sophia.screen.mainloop()

main()
