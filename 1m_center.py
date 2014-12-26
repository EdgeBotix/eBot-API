from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()                    # connect to eBot
myvalue = [0, 0, 0, 0, 0, 0]        # initialize the sonars [ rear left, left, front, right, rear right, back]
myEBot.halt()                       # switches off LED anf motors

#sleep(1)
#
#myEBot.led(1)
#sleep(1)
#myEBot.led(0)
#sleep(1)
#
#myEBot.wheels(.2,.2)
#sleep(2)
#myEBot.halt()
#
#sleep(1)

while():
    sonars = myEBot.robot_uS()              # get the sonars value
    if sonars[2] < 1.000:                   # compare front sonar if it is less than 1 m
        myEBot.wheels(1, -1)               # turn the robot right
    else:
        myEBot.wheels(1, 1)               # else keep moving straight
    print sonars
myEBot.halt()
myEBot.close()