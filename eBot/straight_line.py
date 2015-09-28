from eBot import *
import time
#test
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot.wheels(2, 2)
myEBot.connect()
accel = [0, 0, 0, 0]
myEBot.halt()

myEBot.wheels(0.3, 0.3)
now_time = time.time()
#while accel[1] < 1000:
#    accel = myEBot.position()
#    print acce
while time.time() - now_time < 10:
    accel = myEBot.position()
    print accel
myEBot.wheels(0, 0)
myEBot.halt()
myEBot.close()
