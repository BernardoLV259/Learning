'''

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() == False:
    if wall_in_front():
        turn_around()
    else:
        move()
        turn_left()

'''

#This code was used in https://reeborg.ca/index_en.html