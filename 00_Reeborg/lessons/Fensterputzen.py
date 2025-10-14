from library import turn_right

def main():
    for _ in range(5):
        clean_one_skyscraper()
        
def clean_one_skyscraper():
    move_up_cleaning()
    move_over()
    move_down_cleaning()
    
def move_up_cleaning():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()

def move_over():
    while wall_on_right():
        move()

def move_down_cleaning():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

main()   
