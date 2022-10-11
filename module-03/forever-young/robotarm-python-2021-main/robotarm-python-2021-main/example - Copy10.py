from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
op = 9
po = 8
for aaa in range(5):
    robotArm.grab()
    for x in range(op):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(po):
        robotArm.moveLeft()
    op = op - 2
    po = po - 2
robotArm.wait()