from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:


# for i in range (4):
#     for move in range(4):
#         robotArm.grab()
#         for i in range(5):
#           robotArm.moveRight()
#         robotArm.drop()
#         for i in range(4):
#             robotArm.moveLeft()
#     for move in range(5):
#         robotArm.moveLeft()



for a in range(4):
    for i in range(4):
        robotArm.grab()
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(4):
            robotArm.moveLeft()
    for s in range(5):
        robotArm.moveLeft()


# print(robotArm.scan())
# if robotArm.scan() == '':
#     print('waa')

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()