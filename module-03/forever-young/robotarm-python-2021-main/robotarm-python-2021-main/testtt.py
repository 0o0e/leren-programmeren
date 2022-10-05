from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')
robotArm.speed = (3)

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for move in range (1,8):
  robotArm.grab()
  for move1 in range (move):
    print(robotArm.moveRight())
  robotArm.drop()
  for move1 in range (move):
    print(robotArm.moveLeft())
 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()