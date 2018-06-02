import malmopy
import time

def setup_mission(spec):
    with open('missions/cliff_walking_1.xml', 'r') as mfile:
        spec = malmopython.MissionSpec(mfile.read(), True)
    return spec

malmo = malmopy.Malmo()
malmo.set_delay(0.5)
malmo.setup_mission('missions/cliff_walking_1.xml')
malmo.start_mission()
while malmo.is_running():
    obs = malmo.observe()
    floor = obs['floor']
    print(obs)
    if 'lava' not in floor[(0,1)]:
        malmo.move(1)
    else:
        malmo.turn(-1)
