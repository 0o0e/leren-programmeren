from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:

for bloep in range(7):
    robotArm.moveRight()

for biep in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()