from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
raw_val = [0, 0, 0, 0, 0, 0]
myEBot.halt()
while True:
    print myEBot.acceleration()
myEBot.halt()
myEBot.close()
