from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
sonars = [0, 0, 0, 0]
myEBot.halt()
while True:
    myEBot.wheels(0.2, -0.2)
    now_time = time()
    sonars1 = myEBot.acceleration()
    initial_heading= sonars1[2]
    while initial_heading - sonars[2] < 90:
        sonars = myEBot.acceleration()
        print sonars
    myEBot.wheels(0, 0)
    now_time = time()
    while time() - now_time < 3:
        sonars = myEBot.acceleration()
        print sonars
myEBot.halt()
myEBot.close()
