from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
teller = 9
while teller < 10 and teller > 0:
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for move in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        teller = teller - 1
        for move1 in range(0,teller):
            robotArm.moveLeft()
    if color != 'red':
        robotArm.drop()
        robotArm.moveRight()
        teller = teller - 1
robotArm.wait()