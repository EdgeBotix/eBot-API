YOfrom eBot import *
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
cali_values =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #[Right_pulse/10, Left_pulse/10, LDR_top, LDR_bottom, rear left, left, front, right, rear right, back]
myEBot.connect()
myEBot.halt()
myinput = 0
testing = bool(int(myinput))
nowtime = time.time()

# Get the initial values press 1 for yes, 0 for no

while not testing:
    print "Is the Robot in open light intesity? press 1 for yes, 0 for no"
    myinput = raw_input()
    testing = bool(int(myinput))
cali_values_open = myEBot.calibration_values()      # Get all the values



print "Put the Robot under the test jig shadow"
sleep(1)
myinput = 0
testing = bool(int(myinput))

#get values when under the shed
while not testing:
    print "Is the Robot under test jig? press 1 for yes, 0 for no"
    myinput = raw_input()
    testing = bool(int(myinput))
cali_values_close = myEBot.calibration_values()
top_ldr = cali_values_close[2]
myinput = 0
testing = bool(int(myinput))

#waiting for user to start the code
while not testing:
    print "Start Test? press 1 for yes, 0 for no"
    myinput = raw_input()
    testing = bool(int(myinput))

#keep getting the value unless it passes through the test jig
while True:
    cali_values_now = myEBot.calibration_values()
    print myEBot.calibration_values()               #printing all values
    if top_ldr-0.02 <cali_values_now[2] < top_ldr+0.02 or cali_values_now[6]<0.3:
        myEBot.wheels(0, 0)
    else:
        myEBot.wheels(1, 1)
myEBot.halt()
myEBot.close()
