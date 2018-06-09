import malmopy

malmo = malmopy.Malmo()
malmo.set_delay(0.1)
malmo.setup_mission('missions/cliff_walking_1.xml')
malmo.start_mission()

def act(obs):
    floor = obs['floor']
    print(floor)
    if 'lava' not in floor[(0,1)]:
        print('move')
        malmo.move(1)
    else:
        print('turn left')
        malmo.turn(-1)

malmo.start_agent(act)
malmo.save_gif('cliff.gif')
