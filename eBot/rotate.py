from eBot import *
import time

myBot = eBot()
myBot.connect()
myBot.led(1)
myBot.wheels(-0.1,0.1)
time.sleep(5)
myBot.led(0)
myBot.halt()
myBot.close()
