from eBot import *
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot.connect()
accel = [0, 0, 0, 0, 0, 0]
myEBot.halt()

print myEBot.power()
for i in range(1,300):
    if 0.25 < myEBot.robot_uS()[2] < .3:
        myEBot.wheels(0,0)
    elif myEBot.robot_uS()[2] < .25:
        myEBot.wheels(-1,-1)
    else:
        myEBot.wheels(1,1)
    print myEBot.position()
myEBot.halt()
sleep(3)
print myEBot.position()
myEBot.imperial_march()
myEBot.close()
