def do_robin():
    if object_here():
        take()
    if not object_here():
        put()

while front_is_clear():
    do_robin()
    move()
do_robin()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_around():
    turn_left()
    turn_left()