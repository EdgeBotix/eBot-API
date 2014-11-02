from eBot import *
from time import time

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
myvalue = [0, 0, 0, 0, 0, 0]
myEBot.halt()

sleep(1)
obs = myEBot.obstacle()

myEBot.led(1)
sleep(1)
myEBot.led(0)
sleep(0.5)
myEBot.led(1)

myEBot.wheels(.2,.2)
sleep(2)
myEBot.halt()
sleep(1)
myEBot.wheels(.1,.1)
#sleep(2)
#myEBot.wheels(-1,-1)
#sleep(2)
#myEBot.halt    ()
while True:
    myvalue = myEBot.robot_uS()

    if myvalue[2] < 0.300:
        myEBot.halt()
    else:
        myEBot.wheels(1,1)
    #print myvalue
myEBot.disconnect()
