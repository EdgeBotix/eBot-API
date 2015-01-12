from eBot import *
from time import *
import os
import sys
from serial import Serial
import glob
import time
botList =[]
botNum =5
portsFound =0
myinput = 'y'
for i in range (botNum):
    bot = eBot()
    bot.connect()
    bot.halt()
    botList.append(bot)
while True:
    print "Do you wanna run S script?: y/n"
    mode = raw_input()
    if mode =='y':
        f = open('script_s.txt', 'r')
        myinput=f.next()
        myinput = myinput.split(' ')
        while myinput[0] != "e\n" and myinput[0] != "e":
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
            myinput=f.next()
            myinput = myinput.split(' ')
    else:
        pass
    f.close()

    print "Do you want to correct?: y/n"
    mode = raw_input()
    if mode =='y':
        print ("Set(12345) $ Command (f:b:r:l:e) & time: ")
        myinput = raw_input()
        myinput = myinput.split(' ')
        while myinput[0] != "e\n" and myinput[0] != "e":
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
            print ("Set(12345) $ Command (f:b:r:l:e) & time: ")
            myinput = raw_input()
            myinput = myinput.split(' ')
    else:
        pass

    print "Do you wanna run moving out script?: y/n"
    mode = raw_input()
    if mode =='y':
        f = open('script_u.txt', 'r')
        myinput=f.next()
        myinput = myinput.split(' ')
        while myinput[0] != "e\n" and myinput[0] != "e":
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
            myinput=f.next()
            myinput = myinput.split(' ')
    else:
        pass
    f.close()
    for bot in botList:
        bot.halt()
bot.close()

