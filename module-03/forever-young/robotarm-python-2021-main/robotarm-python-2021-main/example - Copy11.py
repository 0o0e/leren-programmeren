from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for ii in range(9):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()







# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()