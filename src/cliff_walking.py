import malmopy

malmo = malmopy.Malmo()
malmo.set_delay(0.5)
malmo.setup_mission('missions/cliff_walking_1.xml')
malmo.start_mission()
while malmo.is_running():
    obs = malmo.observe()
    floor = obs['floor']
    print(floor)
    if 'lava' not in floor[(0,1)]:
        print('move')
        malmo.move(1)
    else:
        print('turn left')
        malmo.turn(-1)
