from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
for i in range(9):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()