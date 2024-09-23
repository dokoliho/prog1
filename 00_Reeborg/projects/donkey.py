def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def collect_star():
    if object_here():
        take()
     
def collect_all_in_row():
    while front_is_clear():
        collect_star()
        move()
    collect_star()
 
def move_up():
    turn_around()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()


think(3)
for _ in range(8):
    collect_all_in_row()
    move_up()
collect_all_in_row()
