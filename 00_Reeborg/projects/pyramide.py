from library import *

# Konvention fuer alle Kommentare:
#   Reihe 1 = unterste Reihe, Position 1 = linker Rand
#   "Blick Ost" = Reeborg schaut nach rechts


def main():
    # Vor:  steht unten links, Blick Ost, Feld leer
    build_first_row()
    if front_is_clear():          # Feld breiter als 1?
        build_second_row()
        while object_here():
            build_next_row()


def build_first_row():
    # Vor:  steht unten links, Blick Ost
    # Nach: ganze unterste Reihe belegt, steht wieder unten links, Blick Ost
    while front_is_clear():
        put()
        move()
    put()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def build_second_row():
    # Vor:  steht auf dem ersten Stein der untersten Reihe, Blick Ost
    # Nach: zweite Reihe gebaut; steht auf ihrem ersten Stein
    #       (bzw. auf dem leeren Feld, falls sie leer ist), Blick Ost
    move()
    while front_is_clear():
        set_stone_above()
    go_up_facing_west()
    return_to_row_start()


def build_next_row():
    # Vor:  steht auf dem ersten Stein einer Reihe, Blick Ost
    # Nach: Reihe darueber gebaut; steht auf ihrem ersten Stein
    #       (bzw. auf dem leeren Feld, falls sie leer ist), Blick Ost
    move()
    while object_here():
        set_stone_above()
    go_up_facing_west()
    move()
    if object_here():             # ein Stein zu viel gesetzt -> wieder weg
        take()
    return_to_row_start()


def set_stone_above():
    # Vor:  Blick Ost
    # Nach: Stein ueber der alten Position gesetzt,
    #       steht ein Feld weiter rechts in derselben Reihe, Blick Ost
    turn_left()
    move()
    put()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def go_up_facing_west():
    # Vor:  Blick Ost
    # Nach: ein Feld hoeher, Blick West
    turn_left()
    move()
    turn_left()


def return_to_row_start():
    # Vor:  Blick West, steht auf dem leeren Feld direkt rechts der Reihe
    # Nach: steht auf dem ersten Stein der Reihe, Blick Ost
    move()
    while object_here():
        move()
    turn_around()
    move()


think(3)
set_trace_style("invisible")
main()
