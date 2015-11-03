from eBot import *
import time
myEBot = eBot()
myEBot.connect()
print myEBot.power()
myEBot.wheel_calibrate(990,1000)
def Movement(value,r_time):
    wheel_speed = value
    myEBot.wheels(wheel_speed, wheel_speed)
    now_time = time.time()
    while (time.time() < now_time + r_time ):
        print (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        #print (myEBot.position()).__str__().replace('[',' ').replace(']',' ')
        sleep(0.05)
    myEBot.halt()
def main():
    for num in range(100):
        value =input("Enter the rotational speed of the eBot: ")
        r_time = input("Enter the time you want eBot to rotate: ")
        Movement(value,r_time)
    myEBot.close()
main()
