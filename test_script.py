from eBot import *
from time import *
eBot = eBot()
eBot.connect()
eBot.wheels(1,1) #full forward
sleep(1)
eBot.wheels(0,0) #Stop - can use halt as well
sleep(0.5)
eBot.led(1)
eBot.wheels(-1,-1) #full backward
sleep(1)
eBot.halt()
eBot.disconnect()
