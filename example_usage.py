from eBot import *
from time import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()

myEBot.led(1)
sleep(1)
myEBot.led(0)
sleep(0.5)
myEBot.led(1)

myEBot.wheels(1,1)
sleep(2)
myEBot.halt()
sleep(1)
myEBot.wheels(1,1)
sleep(1)
myEBot.disconnect()
