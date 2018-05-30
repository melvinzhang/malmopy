import MalmoPy
import time

if __name__ == "__main__":
    MalmoPy.init()
    ah = MalmoPy.create_agent_host()
    spec = MalmoPy.MissionSpec()
    # with open('default.xml', 'r') as mfile:
    #     spec = MalmoPython.MissionSpec(mfile.read(), True)
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
    record = MalmoPy.MissionRecordSpec()
    MalmoPy.start_mission(ah, spec, record)
    MalmoPy.wait_for_mission_start(ah)
    for i in range(10):
        time.sleep(1)
        cmd = 'move 1'
        ah.sendCommand(cmd)
        print(cmd)
    MalmoPy.wait_for_mission_end(ah)

