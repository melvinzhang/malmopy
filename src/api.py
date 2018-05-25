from __future__ import print_function

from builtins import range
import MalmoPython
import os
import sys
import time

def init():
    if sys.version_info[0] == 2:
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    else:
        import functools
        global print
        print = functools.partial(print, flush=True)
    
    if 'MALMO_XSD_PATH' not in os.environ:
        print('ERROR: MALMO_XSD_PATH not found in env')
        exit(1)

def print_mission_spec():
    my_mission = MalmoPython.MissionSpec()
    print(my_mission.getAsXML(True))

# Create default Malmo objects:
def create_agent_host():
    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse( sys.argv )
    except RuntimeError as e:
        print('ERROR:',e)
        print(agent_host.getUsage())
        exit(1)
    if agent_host.receivedArgument("help"):
        print(agent_host.getUsage())
        exit(0)
    return agent_host

# Attempt to start a mission:
def start_mission(agent_host, my_mission, my_mission_record):
    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission:",e)
                exit(1)
            else:
                time.sleep(2)

def start_default_mission(agent_host):
    my_mission = MalmoPython.MissionSpec()
    my_mission_record = MalmoPython.MissionRecordSpec()
    start_mission(agent_host, my_mission, my_mission_record)

# Loop until mission starts:
def wait_for_mission_start(agent_host):
    print("Waiting for the mission to start ", end=' ')
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)
    print()
    print("Mission running ", end=' ')

# Loop until mission ends:
def wait_for_mission_end(agent_host):
    world_state = agent_host.getWorldState()
    while world_state.is_mission_running:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)

init()
ah = create_agent_host()
spec = MalmoPython.MissionSpec()
#with open('default.xml', 'r') as mfile:
#    spec = MalmoPython.MissionSpec(mfile.read(), True)
spec.setTimeOfDay(12000, False)
spec.startAtWithPitchAndYaw(0.5, 227, 0.5, 0, 90)
spec.drawSphere(-15, 227, 0, 10, 'air')
spec.removeAllCommandHandlers()
spec.allowAllDiscreteMovementCommands()
print(spec.getAsXML(True))
chs = list(spec.getListOfCommandHandlers(0))
for ch in chs:
    cmds = list(spec.getAllowedCommands(0, ch))
    print(ch, cmds)
record = MalmoPython.MissionRecordSpec()
start_mission(ah, spec, record)
wait_for_mission_start(ah)
for i in range(10):
    time.sleep(1)
    cmd = 'move 1'
    ah.sendCommand(cmd)
    print(cmd)
wait_for_mission_end(ah)

