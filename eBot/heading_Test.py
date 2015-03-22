from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
sonars = [0, 0, 0, 0]
myEBot.halt()
while True:
    myEBot.wheels(-1, 1)
    now_time = time()
    sonars1 = myEBot.position()
    initial_heading = sonars1[2]
    while -initial_heading + sonars[2] < 55:
        sonars = myEBot.position()
        print sonars
    myEBot.wheels(0, 0)
    now_time = time()
    while time() - now_time < 5:
        sonars = myEBot.position()
        print sonars
myEBot.halt()
myEBot.close()
