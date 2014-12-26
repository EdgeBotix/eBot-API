from eBot import *
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()
myEBot.connect()
myinput = 1
myEBot.halt()

while True:
    print "Enter the input"
    myinput = raw_input()
    myinput = myinput.replace("[", "")
    myinput = myinput.replace("]]", "")
    getting_data = myinput.split("],")
    for i in range(0, len(getting_data), 1):
        get_command = getting_data[i].split(",")
        if get_command[0] == "'f'":
            myEBot.wheels(0.7, 0.7)
            sleep(int(get_command[1]))
        elif get_command[0] == "'b'":
            myEBot.wheels(-0.7, -0.7)
            sleep(int(get_command[1]))
        elif get_command[0] == "'rac'":
            myEBot.wheels(0, 0.7)
            sleep(int(get_command[1]))
        elif get_command[0] == "'rc'":
            myEBot.wheels(0.7, 0.0)
            sleep(int(get_command[1]))
        else:
            myEBot.halt()
        myEBot.halt()
myEBot.close()
