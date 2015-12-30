from eBot import *
import time
import csv
myBot = eBot()
myBot.connect()
position = myBot.position()
print position
data =[]
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
for i in range(1,100):
        print myBot.robot_uS()[2]
        sleep(0.1)
        data.append(myBot.robot_uS()[2])

path = 'IR'
csv_writer(data, path)

