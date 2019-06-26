from __future__ import print_function

from builtins import range
import os
import sys
import time
import json
#from PIL import Image

# set env var needed by native library
os.environ["MALMO_XSD_PATH"] = os.getcwd() + "/schemas"
import MalmoPython

class Malmo():
    def __init__(self):
        init()
        self.ah = create_agent_host()
        self.spec = MalmoPython.MissionSpec()
        self.record = MalmoPython.MissionRecordSpec()
        self.delay = 0.5
        self.images = []

    def set_delay(self, n):
        self.delay = n

    def setup_mission(self, fun):
        if isinstance(fun, str):
            with open(fun, 'r') as mfile:
                self.spec = MalmoPython.MissionSpec(mfile.read(), True)
        else:
            fun(self.spec)

        # always run mission in third person view
        self.spec.setViewpoint(1)

        #print(spec.getAsXML(True))
        #chs = list(spec.getListOfCommandHandlers(0))
        #for ch in chs:
        #    cmds = list(spec.getAllowedCommands(0, ch))
        #    print(ch, cmds)

    def start_mission(self, fun=None):
        if fun is not None:
            self.setup_mission(fun)
        start_mission(self.ah, self.spec, self.record)
        wait_for_mission_start(self.ah)

    def end_mission(self):
        wait_for_mission_end(self.ah)

    def send_command(self, command):
        self.ah.sendCommand(command)
        time.sleep(self.delay)

    def move(self, n=1):
        self.send_command("move " + str(n))
        self._wait_for_update()

    def turn(self, n):
        self.send_command("turn " + str(n))
        self._wait_for_update()

    def turn_left(self):
        self.turn(-1)

    def turn_right(self):
        self.turn(1)

    def observe(self):
        ws = self.ah.getWorldState()
        while ws.is_mission_running and (len(ws.observations) == 0 or len(ws.video_frames) == 0):
            time.sleep(0.1)
            ws = self.ah.peekWorldState()
        if not ws.is_mission_running:
            return None
        obs = json.loads(ws.observations[-1].text)
        if 'floor' in obs and len(obs['floor']) == 9 and 'Yaw' in obs:
            obs['floor'] = relative_blocks(obs['floor'], obs['Yaw'])
        frame = ws.video_frames[-1]
        #image = Image.frombytes('RGB', (frame.width, frame.height), bytes(frame.pixels) )
        #self.images.append(image)
        return obs

    def is_running(self):
        return self.ah.peekWorldState().is_mission_running

    def _wait_for_update(self):
        while True:
            time.sleep(0.001)
            ws = self.ah.getWorldState()
            if ws.number_of_observations_since_last_state > 0 or not ws.is_mission_running:
                break

    def save_gif(self, path):
        self.images[0].save(path, save_all=True, append_images=self.images[1:], duration=300)

    # uses a callback act
    def start_agent(self, act):
        while self.is_running():
            obs = self.observe()
            if obs is not None:
                act(obs)

    # generator of observations
    def observations(self):
        while self.is_running():
            obs = self.observe()
            if obs is not None:
                yield obs

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
    print(" started")

# Loop until mission ends:
def wait_for_mission_end(agent_host):
    world_state = agent_host.getWorldState()
    while world_state.is_mission_running:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)

def relative_blocks(blocks, y):
    def rotate(l, n):
        return l[n:]+ l[:n]

    yaw = [0, 90, 180, 270]
    front = [7, 3, 1, 5]
    front_right = [6, 0, 2, 8]
    pos = {
        (0,0): [4, 4, 4, 4],
        #front
        (0,1): rotate(front, 0),
        #right
        (1,0): rotate(front, 1),
        #back
        (0,-1): rotate(front, 2),
        #left
        (-1,0): rotate(front, 3),
        #front_right:
        (1,1): rotate(front_right, 0),
        #back_right:
        (1,-1): rotate(front_right, 1),
        #back_left:
        (-1,-1): rotate(front_right, 2),
        #front_left:
        (-1,1): rotate(front_right, 3)
    }

    res = {}
    idx = yaw.index(y)
    for k,v in pos.items():
        res[k] = blocks[v[idx]]

    return res
