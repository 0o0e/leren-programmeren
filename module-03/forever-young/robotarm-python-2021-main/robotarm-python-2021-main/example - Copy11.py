from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
teller = 9
robotArm.speed = 3
for move  in range (teller):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == '':
        break
    if robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
        teller = teller 
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()