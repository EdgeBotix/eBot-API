import math
from time import *
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as eBotsonarDist

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.7
forwardVelocity = 0.1
#k1 = 100
#k2 = -97.9748

#k1 = 30
#k2 = -29.7715

k1 = 100
k2 = -98.7258

#k1 = 300
#k2 = -271.73

# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        sonars = inp.sonars
        v = eBotsonarDist.getDistanceRight(inp.sonars)
        return (state, v)

# inp is the distance to the right
class WallFollower(sm.SM):
    #startState = desiredRight
    startState = None
    def getNextValues(self, state, inp):

        if state == None:
            state = inp
        do = inp
        di = desiredRight
        e  = di - do
        e2 = di - state
        rvel = k1*e + k2 * e2
        state = inp
        if rvel > 1:
            rvel =1
        elif rvel <-1:
            rvel= -1
        sleep(0.05)
        print inp, e, e2, rvel
        #print "w[n]   e[n]  e[n-1]", rvel, e , e2       
        return (state, io.Action(forwardVelocity, rvel))

sensorMachine = Sensor()
sensorMachine.name = 'sensor'
mySM = sm.Cascade(sensorMachine, WallFollower())

######################################################################
#
#            Running the robot
#
######################################################################
def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x:x))
    robot.behavior = mySM
    #robot.behavior.start(traceTasks = robot.gfx.tasks())
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())
def step():
    inp = io.SensorInput()
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())
def brainStop():
    pass
