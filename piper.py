import sys
sys.path.insert(0, 'C:\Users\Erik Wilhelm\Documents\GitHub\eBot-API') #Insert your directory for the eBot-API here

from eBot import *

myEBot = eBot()
myEBot.connect()

freq = [100, 400, 700]          # Freq. in Hz
time = [500, 500, 500]   # Time in MS

for f, t in zip(freq, time):
    myEBot.buzzer(t, f)
    print(t, f)

myEBot.close()