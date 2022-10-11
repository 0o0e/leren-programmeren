from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
aa = 1
while True:
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == '':
        break
    for o in range(aa):
        robotArm.moveRight()
    aa = aa + 1
    robotArm.drop()
    for o in range(aa):
        robotArm.moveLeft()
robotArm.wait()