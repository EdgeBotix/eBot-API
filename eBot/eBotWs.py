from eBot import *
import time
import random
import string
import cherrypy

class eBotWs(object):
    _cp_config = {'tools.sessions.on': True}

    def __init__(self):
        self.mybot = eBot()

    @cherrypy.expose
    def connect(self):
        if self.mybot is not None:
            self.mybot.connect()
            print self.mybot.power()
            return '''Success Connect.'''

    @cherrypy.expose
    def disconnect(self):
        self.mybot.close()
        return '''Success Disconnect.'''

    @cherrypy.expose
    def movement(self, value, r_time):
        wheel_speed = value
        self.mybot.wheels(wheel_speed, wheel_speed)
        now_time = time.time()
        while (time.time() < now_time + r_time ):
            print (self.mybot.robot_uS()).__str__().replace('[',' ').replace(']',' ')
            sleep(0.05)
        self.mybot.halt()

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
    cherrypy.quickstart(eBotWs())