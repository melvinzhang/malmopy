import malmopy
import time

def setup_mission(spec):
    # with open('default.xml', 'r') as mfile:
    #     spec = malmopython.MissionSpec(mfile.read(), True)
    spec.setTimeOfDay(12000, False)
    spec.startAtWithPitchAndYaw(0.5, 227, 0.5, 0, 90)
    spec.drawSphere(-15, 227, 0, 10, 'air')
    spec.removeAllCommandHandlers()
    spec.allowAllDiscreteMovementCommands()

if __name__ == "__main__":
    malmo = malmopy.Malmo()
    malmo.setup_mission(setup_mission)
    malmo.start_mission()
    for i in range(10):
        malmo.move(1)
        print("move 1")
    malmo.end_mission()
    print("mission end")

