from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 2
for move in range(7):
    robotArm.moveRight()
for move in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.wait()