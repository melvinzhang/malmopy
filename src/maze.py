import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/maze_1.xml')

for obs in malmo.observations():
    floor = obs['floor']
    print(floor)
    # left hand rule: always keep the wall on the left
    # left side is empty, turn in
    if floor[(-1,0)] == 'air':
        malmo.turn(-1)
        malmo.move(1)
    # left is blocked, front is empty
    elif floor[(0,1)] == 'air':
        malmo.move(1)
    # left is blocked, front is blocked
    else:
        malmo.turn(1)
