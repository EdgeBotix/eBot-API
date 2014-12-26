from eBot import *
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot.connect()
myinput = 1
myEBot.halt()

while True:
    print "Number of times robot should run"
    myinput = raw_input()
    if int(myinput) < 1:
        print "Value entered must be bigger than zero"
    else:
        right_throttle = -0.7
        left_throttle = -0.7
        for i in range(0, int(myinput), 1):
            right_throttle = -right_throttle
            left_throttle = -left_throttle
            nowtime = time.time()
            while time.time() < nowtime + 2:
                sonars = myEBot.robot_uS()
                if sonars[2] > 0.6:
                    myEBot.wheels(left_throttle, right_throttle)
                else:
                    myEBot.wheels(-1, 1)
            myEBot.halt()
myEBot.close()
