from eBot import *
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot.connect()
accel = [0, 0, 0, 0, 0, 0]
myEBot.halt()
while accel[1] < 100:
    accel = myEBot.robot_uS()
    sleep(0.05)
    print accel

now_time = time.time()
while time.time() - now_time < 5:
    accel = myEBot.position()
    print accel
myEBot.halt()
myEBot.close()
