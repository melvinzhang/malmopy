import MalmoPy
import time

def setup_mission(spec):
    # with open('default.xml', 'r') as mfile:
    #     spec = MalmoPython.MissionSpec(mfile.read(), True)
    spec.setTimeOfDay(12000, False)
    spec.startAtWithPitchAndYaw(0.5, 227, 0.5, 0, 90)
    spec.drawSphere(-15, 227, 0, 10, 'air')
    spec.removeAllCommandHandlers()
    spec.allowAllDiscreteMovementCommands()

if __name__ == "__main__":
    malmo = MalmoPy.Malmo()
    malmo.setup_mission(setup_mission)
    malmo.start_mission()
    malmo.wait_for_mission_start()
    print("mission start")
    for i in range(10):
        time.sleep(1)
        malmo.move(1)
        print("move 1")
    malmo.wait_for_mission_end()
    print("mission end")

