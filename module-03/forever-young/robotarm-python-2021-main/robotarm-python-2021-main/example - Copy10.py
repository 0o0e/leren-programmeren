from multiprocessing.connection import wait
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
right = 9
left = 8
for aaa in range(5):
    robotArm.grab()
    for x in range(right):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(left):
        robotArm.moveLeft()
    right = right - 2
    left = left - 2
robotArm.wait()
 