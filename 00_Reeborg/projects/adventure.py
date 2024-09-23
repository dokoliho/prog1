from library import turn_right
        
while wall_on_right():
    move()
turn_left()
turn_left()
move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    for _ in range(3):
        turn_left()