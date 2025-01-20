def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    else:
        jump()
    
   
   