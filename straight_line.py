from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
accel = [0, 0, 0, 0]
myEBot.halt()

myEBot.wheels(1, 1)
now_time = time()
while accel[1] < 1000:
    accel = myEBot.position()
    print accel
myEBot.wheels(0, 0)
now_time = time()
while time() - now_time < 5:
    accel = myEBot.position()
    print accel
myEBot.halt()
myEBot.close()
