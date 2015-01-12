from eBot import *
from time import *
import os
import sys
from serial import Serial
# import serial
import glob
import time
#Create new instance of eBot - connects to first eBot the computer is connected to
botList =[]
botNum =5
portsFound =0
for i in range (botNum):
    bot = eBot()
    bot.connect()
    bot.halt()
    botList.append(bot)

print "Do you wanna run a script?: y/n"
mode = raw_input()
if mode =='n':
    f = open('script.txt', 'w')
else:
    f = open('script.txt', 'r')

while True:
    if mode =='n':
        print ("Set(12345) $ Command (f:b:r:l:e) & time: ")
        myinput = raw_input()
        f.write(myinput+'\n')
    else:
        myinput=f.next()
    myinput = myinput.split(' ')
    print myinput[0]
    if myinput[0] == "e\n" or myinput[0] == "e":
        f.close()
        print ("run a script?y/n")
        mode = raw_input()
        if mode =="y":
            f = open('script.txt', 'r')
        else:
            for bot in botList:
                bot.close()
            break
    else:
        try:
            if myinput[1] == "f":
                for i in list(myinput[0]):
                    botList[int(i)].wheels(float(myinput[3]),float(myinput[4]))
                sleep(float(myinput[2]))
            if myinput[1] == "b":
                for i in list(myinput[0]):
                    botList[int(i)].wheels(-float(myinput[3]),-float(myinput[4]))
                sleep(float(myinput[2]))
            if myinput[1] == "l":
                for i in list(myinput[0]):
                    botList[int(i)].wheels(-1,1)
                sleep(float(myinput[2]))
            if myinput[1] == "r":
                for i in list(myinput[0]):
                    botList[int(i)].wheels(1,-1)
                sleep(float(myinput[2]))
            if myinput[1] == "t":
                for i in list(myinput[0]):
                    botList[int(i)].turn(float(myinput[2]))
        except:
            print "ya'll messed up"
        for bot in botList:
            bot.halt()



