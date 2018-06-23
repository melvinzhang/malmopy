import malmopy

malmo = malmopy.Malmo()
malmo.start_mission('missions/cliff_walking_1.xml')

for obs in malmo.observations():
    floor = obs['floor']
    print(floor)
    if 'lava' not in floor[(0,1)]:
        print('move')
        malmo.move(1)
    else:
        print('turn left')
        malmo.turn(-1)
