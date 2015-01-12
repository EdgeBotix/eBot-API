from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
print myEBot.power()
print myEBot.temperature()
myEBot.wheels(1, 1)
print myEBot.robot_uS()
sleep(1)
print myEBot.power()
myEBot.close()
