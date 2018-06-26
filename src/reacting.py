import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/cliff_walking_1.xml')

for obs in malmo.observations():
    floor = obs['floor']

    # (0,1) means in front
    # (-1,0) is to the left
    # (1,0) is to the right

    # front is a string description of the block
    front = floor[(0,1)]

    # implement the following logic:
    # if front is safe, i.e. not lava
    #   move forward
    # else
    #   turn left
