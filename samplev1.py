from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
myvalue = [0, 0, 0, 0, 0, 0]
myEBot.halt()

temp = myEBot.temperature()
print temp
myEBot.led(1)
sleep(1)
myEBot.led(0)
sleep(1)
myEBot.wheels(.2,.2)
sleep(2)
myEBot.halt()
sleep(1)

#for i in range(1, 1000, 1):
 #     myEBot.halt()
  #  else:
   #     myEBot.wheels(1, 1)
   # print sonars
myEBot.halt()
myEBot.imeprial_march()
myEBot.close()
