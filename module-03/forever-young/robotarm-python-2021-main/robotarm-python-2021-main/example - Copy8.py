from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
aaa = 0
while aaa < 7:
    for i in range(8):
        robotArm.grab() , robotArm.moveRight()
    robotArm.drop()
    for x in range (8):
        robotArm.moveLeft()
    aaa = aaa + 1
robotArm.wait()