def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def turn_around():
    turn_left()
    turn_left()
    
    
def set_stone_above():
    turn_left()
    move()
    put()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

def build_first_row():
    while front_is_clear():
        put()
        move()
    put()
    turn_around()
    while front_is_clear():
        move()
    turn_around()

    
def build_second_row():
    move()
    while front_is_clear():
        set_stone_above()
    turn_left()
    move()
    turn_left()
    move()
    while object_here():
        move()
    turn_around()
    move()

    
def build_next_row():
    move()
    while object_here():
        set_stone_above()
    turn_left()
    move()
    turn_left()
    move()
    if object_here():
        take()
    move()
    while object_here():
        move()
    turn_around()
    move()

    
think(3)  
set_trace_style("invisible")
build_first_row()
build_second_row()
while object_here():
    build_next_row()
