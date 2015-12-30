from eBot import *
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
myEBot = eBot()
myEBot.connect()
myfile ='ebot044.csv'
print myEBot.power()
#myEBot.wheel_calibrate(980,1020)
value1 = [[]]
data =[]
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
#----------------------------------------------------------------------

def main():
    sonar_values = myEBot.robot_uS()
    position = myEBot.position()

    while (position[0] < 1.1 or sonar_values[2] > 0.3 ):
        sonar_values = myEBot.robot_uS()
        position = myEBot.position()
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        #print (myEBot.position()).__str__().replace('[',' ').replace(']',' ')
        myEBot.wheels(1,1)
    while (position[0]>1.1 and position[2] <140):
        sonar_values = myEBot.robot_uS()
        position = myEBot.position()
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        myEBot.wheels(-0.5,0.5)
    while (sonar_values[2] > 0.3 ):
        sonar_values = myEBot.robot_uS()
        position = myEBot.position()
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        error = 180 - position[2]
        if error>180:
            error= error-360
        myEBot.wheels(0.8 - error/100,0.8 + error/100)
    for i in range(1,50,1):
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        myEBot.wheels(0,0)
    path = myfile
    csv_writer(data, path)
    myEBot.halt()
    myEBot.close()
    data1 = np.genfromtxt(myfile,delimiter=',', dtype = float)
    Left = [row[0] for row in data1]
    front_left = [row[1] for row in data1]
    front = [row[2] for row in data1]
    front_right = [row[3] for row in data1]
    right = [row[4] for row in data1]
    back = [row[5] for row in data1]
    x_position = [row[6] for row in data1]
    y_position = [row[7] for row in data1]
    thetha = [row[8] for row in data1]

    for i in range(0, len(thetha)):
        if -180 < thetha[i] and thetha[i] <= -90:
            thetha[i] += 360
    ldr_front = [row[9] for row in data1]
    ldr_top = [row[10] for row in data1]

    xarray = range(0, len(front))

    plt.subplot(4,3,1)
    plt.plot(xarray, Left)
    plt.title('Left Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,2)
    plt.plot(xarray, front_left)
    plt.title('Front Left Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,3)
    plt.plot(xarray, front)
    plt.title('Front Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,4)
    plt.plot(xarray, front_right)
    plt.title('Front Right Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,5)
    plt.plot(xarray, right)
    plt.title('Right Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,6)
    plt.plot(xarray, back)
    plt.title('Back Sonar')
    plt.ylabel('Distance in M')
    plt.ylim((0,2.5))
    plt.subplot(4,3,7)
    plt.plot(xarray, x_position)
    plt.title('X postion')
    plt.ylabel('Distance in M')
    plt.ylim((-1,2))
    plt.subplot(4,3,8)
    plt.plot(xarray, y_position)
    plt.title('Y postion')
    plt.ylabel('Distance in M')
    plt.ylim((-1,2))
    plt.subplot(4,3,9)
    plt.plot(xarray, thetha)
    plt.title('Theta')
    plt.ylabel('Angle in Deg')
    plt.subplot(4,3,10)
    plt.plot(xarray, ldr_front)
    plt.title('Front LDR')
    plt.ylabel('Value in scale (0,1)')
    plt.subplot(4,3,11)
    plt.plot(xarray, ldr_top)
    plt.title('Top LDR')
    plt.ylabel('Value in scale (0,1)')
    plt.show()
main()


