from eBot import *
import csv
import time
myEBot = eBot()
myEBot.connect()
print myEBot.power()
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

    while (position[0] < 1.1 and sonar_values[2] > 0.3 ):
        sonar_values = myEBot.robot_uS()
        position = myEBot.position()
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        #print (myEBot.position()).__str__().replace('[',' ').replace(']',' ')
        myEBot.wheels(1,1)
    while position[0]>1.1 and position[2] <140 :
        sonar_values = myEBot.robot_uS()
        position = myEBot.position()
        myEBot.wheels(-0.5,0.5)
    while (sonar_values[2] > 0.3 ):
        sonar_values = myEBot.robot_uS()
        value1 = (myEBot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
        value1 = value1+ ',' + myEBot.position().__str__().replace('(',' ').replace(')',' ')+ ',' + myEBot.light().__str__().replace('[',' ').replace(']',' ')
        print value1
        data.append(value1.split(","))
        #print (myEBot.position()).__str__().replace('[',' ').replace(']',' ')
        myEBot.wheels(1,1)
    myEBot.wheels(0,0)
    path = "output.csv"
    csv_writer(data, path)
    myEBot.halt()
    myEBot.close()
main()

