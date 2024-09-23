def repair_stone():
    if object_here():
        pass
    else:
        put()

def repair_pillar():
    turn_left()
    while front_is_clear():
        repair_stone()
        move()
    repair_stone()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    move()

think(0)
for _ in range(3):
    move()
    move()
    repair_pillar()

            