from turtle import Turtle



sophia = Turtle()
zoe = Turtle()

sophia.screen.bgcolor('grey')

sophia.pencolor('black')
sophia.fillcolor('black')
zoe.pencolor('white')
zoe.fillcolor('white')


zoe.begin_fill()
zoe.left(90)
zoe.penup()
zoe.forward(300)
zoe.left(90)
zoe.circle(150, 180)
zoe.end_fill()

sophia.begin_fill()
sophia.circle(150, 180)
sophia.penup()
sophia.left(90)
sophia.forward(300)
sophia.left(90)
sophia.end_fill()

zoe.penup()
zoe.left(90)
zoe.forward(150)
zoe.right(90)
zoe.pendown()
zoe.begin_fill()
zoe.circle(75,180)
zoe.left(90)
zoe.forward(150)
zoe.end_fill()

sophia.pendown()
sophia.begin_fill()
sophia.left(90)
sophia.forward(150)
sophia.left(90)
sophia.circle(75,180)
sophia.end_fill()

zoe.penup()
zoe.forward(85)
zoe.left(90)
zoe.pendown()
zoe.begin_fill()
zoe.circle(10)
zoe.end_fill()

sophia.penup()
sophia.left(90)
sophia.forward(235)
sophia.left(90)
sophia.pendown()
sophia.begin_fill()
sophia.circle(10)
sophia.end_fill()

sophia.hideturtle()
zoe.hideturtle()
sophia.screen.mainloop()