def turn_right():
    turn_left()
    turn_left()
    turn_left()
def trace_path():
    move()
    turn_left()   
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()   

#step = 1
for step in range(1,7):
    trace_path()

#or could be this way
#for step in range(6):
#    trace_path()

#using while loop
hurdles = 6
while hurdles > 0:
    trace_path()
    hurdles = hurdles - 1
    print(hurdles)

#when there is a hurdle randomly
def wall_front():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() == False:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        wall_front()

#hurdle 4:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_down():
    turn_right()
    move()
    turn_right()
    move()

while at_goal() == False:
    if right_is_clear() == True:
        move_down()
    elif front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        turn_left()
