def take_if_there():
    if object_here():
        take()


for _ in range(9):
    take_if_there()
    move()
take_if_there()
