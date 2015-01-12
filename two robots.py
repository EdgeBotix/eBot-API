from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot1 = eBot()
myEbot2 = eBot()
myEBot1.connect()
myEbot2.connect()
myvalue = [0, 0, 0, 0, 0, 0]
myEBot1.halt()

sleep(1)

myEBot1.led(1)
sleep(1)
myEBot1.led(0)
sleep(1)

myEBot1.wheels(.2,.2)
sleep(2)
myEBot1.halt()
sleep(1)

for i in range(1, 1000, 1):
    sonars = myEBot1.robot_uS()
    if sonars[2] < 0.300:
        myEBot1.wheels(-1, -1)
    else:
        myEBot1.wheels(1, 1)
    sonars2 = myEbot2.robot_uS()
    if sonars2[2] < 0.300:
        myEbot2.wheels(-1, -1)
    else:
        myEbot2.wheels(1, 1)
    print sonars

myEBot1.halt()
myEBot1.close()
