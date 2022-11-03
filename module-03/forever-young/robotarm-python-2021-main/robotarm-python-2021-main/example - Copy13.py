from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
position = 1
while True:
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == '':
        break
    for o in range(position):
        robotArm.moveRight()
    position += 1
    robotArm.drop()
    for o in range(position):
        robotArm.moveLeft()
robotArm.wait()