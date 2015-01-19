

from eBot import *
from time import *
eBot = eBot()
eBot.connect()

#Test 6 Sonars

eBot.wheels(0.5,-0.5) #full forward
sleep(10)
eBot.wheels(0,0) #Stop - can use halt as well
sonars = eBot.robot_uS()
print sonars

#Test motors



#Calibrate Encoders


#Test Buzzer


#Test LEDs


#Test LDRs


#Test IMU


#Test Discharge rate


eBot.halt()
eBot.disconnect()

