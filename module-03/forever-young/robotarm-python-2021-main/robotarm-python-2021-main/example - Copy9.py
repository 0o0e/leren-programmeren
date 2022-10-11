from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

for a in range(4):
    for i in range(4):
        robotArm.grab()
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(4):
            robotArm.moveLeft()
    for s in range(5):
        robotArm.moveLeft()
robotArm.wait()