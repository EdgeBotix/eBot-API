
import sys
sys.path.insert(0, 'C:\Users\Robot\Desktop\EdgeBotix\eBot\Software\eBot-API\eBot')
from eBot import *
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()

sonars = [0, 0, 0]
current_time = time()
myEBot.halt()
print myEBot.position()
myEBot.wheels(-0.5, 0.5)
now_time = time()
sonars1 = myEBot.position()
initial_heading = sonars1[2]
while -initial_heading + (sonars[2]) < 180:
    sonars = myEBot.position()
    sleep(0.05)
    print sonars
print time()
myEBot.wheels(0, 0)
now_time = time()
while time() - now_time < 1:
    sonars = myEBot.position()
    sleep(0.05)
    print sonars
    #print time()
print myEBot.power()
print time()
myEBot.halt()
sleep(2)
print myEBot.position()
print myEBot.temperature()
myEBot.close()
