import eBot
import math
import time
import matplotlib.pyplot as plt
myEBot= eBot.eBot()
myEBot.connect()
print myEBot.power()
plt.axis([-5, 5, -5, 5])
plt.ion()
plt.show()
#myEBot.wheel_calibrate(1000,980)

def main():

    for i in range(0,1000):
        sonar_values = myEBot.robot_uS()
        if sonar_values[2] < .3:
            myEBot.wheels(-0.5,0.5)
        else:
            myEBot.wheels(0.5,0.5)
        myposition = myEBot.position()
        sonar_values = myEBot.robot_uS()
        if 0.19 <sonar_values[2] < 0.8:
            obstacle_x = -myposition[1] + sonar_values[2]*math.cos((myposition[2]+90)*math.pi/180)
            obstacle_y = myposition[0] + sonar_values[2]*math.sin((myposition[2]+90)*math.pi/180)
        else:
            obstacle_x =1000
            obstacle_y =1000
        if 0.19 < sonar_values[0] < 2.4:
            obstacle_x1 = -myposition[1] + sonar_values[0]*math.cos((myposition[2]+180)*math.pi/180)
            obstacle_y1 = myposition[0] + sonar_values[0]*math.sin((myposition[2]+180)*math.pi/180)
        else:
            obstacle_x1 =1000
            obstacle_y1 =1000
        if 0.19 < sonar_values[4] < 2.4:
            obstacle_x2 = -myposition[1] + sonar_values[4]*math.cos((myposition[2])*math.pi/180)
            obstacle_y2 = myposition[0] + sonar_values[4]*math.sin((myposition[2])*math.pi/180)
        else:
            obstacle_x2 =1000
            obstacle_y2 =1000
        print sonar_values
        plt.scatter(obstacle_x,obstacle_y, color='blue')
        plt.scatter(obstacle_x1,obstacle_y1, color='blue')
        plt.scatter(obstacle_x2,obstacle_y2, color='blue')
        plt.scatter(-myposition[1],myposition[0], color = 'red')
        plt.draw()
        time.sleep(0.05)
    myEBot.halt()
main()
