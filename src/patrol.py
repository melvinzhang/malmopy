import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/patrol.xml')

for obs in malmo.observations():
    floor = obs['floor']

    # (0,1) means in front
    # (-1,0) is to the left
    # (1,0) is to the right

    # front is a string description of the block
    front = floor[(0,1)]

    # implement the following logic:
    #   patrol the platform in a clockwise direction by
    #   keeping the lava to your left
