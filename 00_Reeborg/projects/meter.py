def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def set_stars():
    move()
    while wall_on_right():
        put()
        move()

def move_to_start():
    turn_right()
    move()
    turn_right()
    while right_is_clear():
     move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    
def move_to_last_star():
    while object_here():
        move()
    turn_around()
    move()
    turn_around()

def move_to_end():
    while front_is_clear():
        move()
    
def count_stars():
    move_to_start()
    while object_here():
        move_to_last_star()
        if object_here():
            take()
            move_to_end()
            put()
            move_to_start()

        
set_stars()
count_stars()

