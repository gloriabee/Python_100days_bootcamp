def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while front_is_clear() and right_is_clear():
    move()

while not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        else:
            turn_left()
   
   