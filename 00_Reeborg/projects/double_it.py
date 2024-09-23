def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def double_star():
    take()
    move()
    put()
    put()
    turn_around()
    move()
    turn_around()

def double_all_stars():
    while object_here():
        double_star()

def move_star():
    take()
    move()
    put()
    turn_around()
    move()
    turn_around()

def move_all_stars():
    while object_here():
        move_star()
        

move()
double_all_stars()
move()
turn_around()
move_all_stars()
move()
move()
