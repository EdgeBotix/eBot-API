from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot2 = eBot()
myEBot.connect()                    # connect to eBot
myEBot2.connect()                    # connect to eBot
myvalue = [0, 0, 0, 0, 0, 0]        # initialize the sonars [ rear left, left, front, right, rear right, back]
myEBot.halt()                       # switches off LED anf motors
myEBot2.halt()
while True:
    #sonars = myEBot.robot_uS()
    #sonars2 = myEBot2.robot_uS()              # get the sonars value
    print "Move Robot"
    raw_input()
    myEBot.wheels(1, 1)
    myEBot2.wheels(0.5, 0.5)
    sleep(3)
    myEBot.halt()
    myEBot2.halt()
    sonars = myEBot.acceleration()
    sonars2 = myEBot2.acceleration()
   # if sonars[2] < 1.000:                   # compare front sonar if it is less than 1 m
   #     myEBot.wheels(1, -1)               # turn the robot right
   # else:
   #     myEBot.wheels(1, 1)               # else keep moving straight
    print sonars
    sleep(1)
    print sonars2
myEBot2.halt()
myEBot2.close()