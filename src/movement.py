import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/cliff_walking_1.xml')

# Sample movement commands.
# Edit it so that the agent moves to where the diamond is.  

# turn right
malmo.turn_right()
# move forward
malmo.move()
# move forward
malmo.move()
# move forward
malmo.move()
# turn left
malmo.turn_left()
