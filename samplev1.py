from eBot import *

#Create new instance of eBot - connects to first eBot the computer is connected to
myEBot = eBot()

myEBot.connect()
print myEBot.power()
print myEBot.temperature()
print myEBot.robot_uS()
print myEBot.light()
#myEBot.buzzer(2000,5000)
#myEBot.buzzer(1000,99)
#myEBot.imperial_march()
myEBot.close()
