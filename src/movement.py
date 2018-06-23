import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/cliff_walking_1.xml')

# Sample movement commands.
# Edit it so that the agent moves to where the diamond is.  

# turn right
malmo.turn(1)
# move forward
malmo.move(1)
# turn left
malmo.turn(-1)
