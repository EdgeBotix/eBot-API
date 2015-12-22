from time import *
import os
import sys
from serial import Serial
from math import degrees, pi
import glob
from Tkinter import *
import tkMessageBox
import Tkinter
from threading import Thread
from Locator_EKF import Locator_EKF


if os.name == 'nt':
    try:
        import _winreg as winreg
    except:
        pass


class eBot():
    def __init__(self):
        self.sonarValues = [0, 0, 0, 0, 0, 0]
        self.all_Values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.port = None
        self.serialReady = False
        self.ldrvalue = [0, 0]
        self.p_value = [0, 0]
        self.acc_values = [0, 0, 0, 0, 0, 0]
        self.pos_values = [0, 0, 0]
        self.EKF = Locator_EKF([0.,0.],0.)
        self.offset_counter = 0
        self.thread_flag = 0
        self.heading =0.
        self.offset_counter_iteration = 100

    def destroy(self):
        """
        Destructor function for eBot class.
        """
        self.disconnect()
        self.sonarValues = None
        self.port = None
        self.serialReady = None

    def getOpenPorts(self):
        """
        Windows only function: Obtains a list of tuples with eBot-relevant port number and description.

        :rtype: list
        :return: devicePorts: list of port numbers and descriptions of relevant serial devices.
        """
        path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        ports = []
        #maximum 256 entries, will break anyways
        for i in range(256):
            try:
                val = winreg.EnumValue(key, i)
                port = (str(val[1]), str(val[0]))
                ports.append(port)
            except Exception:
                winreg.CloseKey(key)
                break
        #return ports
        #ports = getOpenPorts()
        devicePorts = []
        for port in ports:
            #Just because it is formatted that way...
            if 'BthModem' in port[1][8:] or 'VCP' in port[1][8:] or 'ProlificSerial' in port[1][8:]:
                devicePorts.append((int(port[0][3:]) - 1))
        return devicePorts

    def open(self):
        """
        Opens connection with the eBot via BLE. Connects with the first eBot that the computer is paired to.

        :raise Exception: No eBot found
        """
        self.connect()

    def connect(self):
        """
        Opens connection with the eBot via BLE. Connects with the first eBot that the computer is paired to.

        :raise Exception: No eBot found
        """
        baudRate = 115200
        ports = []
        if os.name == "posix":
            if sys.platform == "linux2":
                #usbSerial = glob.glob('/dev/ttyUSB*')
                ports = glob.glob('/dev/rfcomm*')
                #print "Support for this OS is under development."
            elif sys.platform == "darwin":
                ports = glob.glob('/dev/tty.eBo*')
                #usbSerial = glob.glob('/dev/tty.usbserial*')
            else:
                print "Unknown posix OS."
                sys.exit()
        elif os.name == "nt":
            ports = self.getOpenPorts()
            #ports = ['COM' + str(i + 1) for i in range(256)]
            #EBOT_PORTS = getEBotPorts()

        connect = 0
        ebot_ports = []
        ebot_names = []
        line = "a"
        print "connecting",
        for port in ports:
            try:
                print ".",
                if (line[:2] == "eB"):
                    break
                s = Serial(port, baudRate, timeout=5.0, writeTimeout=5.0)
                s._timeout = 5.0
                s._writeTimeout = 5.0
                #try:
                #    s.open()
                #except:
                #    continue

                while (line[:2] != "eB"):
                    if (s.inWaiting()>0):
                        line=s.readline()
                    s.write("<<1?")
                    sleep(0.5)
                    line = s.readline()
                    if (line[:2] == "eB"):
                        ebot_ports.append(port)
                        ebot_names.append(line)
                        connect = 1
                        self.port = s
                        self.portName = port
                        self.port._timeout = 5.0
                        self.port._writeTimeout = 5.0
                        self.port.flushInput()
                        self.port.flushOutput()
                        break
                    #s.close()
                #                    self.
            except:
                try:
                    if s.isOpen():
                        s.close()
                except:
                    pass

        if (connect == 0):
            try:
                self.port.close()
            except:
                pass
            #sys.stderr.write("Could not open serial port.  Is robot turned on and connected?\n")
            print "Connection Error", "No eBot found. Please reconnect and try again.",
            #import ctypes  # An included library with Python install.
            #ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
            raise Exception("No eBot found")

        sleep(.01)
        try:
            self.port.write('<<1E')
            sleep(0.4)
            line = self.port.readline()
            if (line != ">>1B\n" and line != ">>1B" and line != ">>\n" and line != ">>"):
                self.lostConnection()
            self.port.write("<<1O")
            sleep(0.4)
            self.port.write("F")
            sleep(0.2)
            self.port.flushInput()
            self.port.flushOutput()
            print "connected"
            self.receive_thread = Thread(target= self.recieve_background)
            self.thread_flag =1
            self.receive_thread.start()
            self.offset_counter =0


        except:
            print "COM Error", "Robot connection lost..."
            sys.stderr.write("Could not write to serial port.\n")
            self.serialReady = False
            sys.stderr.write("Robot turned off or no longer connected.\n")
        sleep(7)
        self.serialReady = True


    def read(self):
        self.incoming=None
        if self.offset_counter>1:
            self.prev_time_stamp = self.time_stamp
        if self.port.inWaiting()!=0:
            self.incoming=self.port.readline().rstrip('\n')
            self.offset_counter += 1
            try:
                self.time_stamp , self.Ax , self.Ay , self.Az , self.Gx , self.Gy , self.Gz , \
                    self.Ultrasonic_rear_right, self.Ultrasonic_right, self.Ultrasonic_front , \
                    self.Ultrasonic_left , self.Ultrasonic_rear_left , self.Ultrasonic_back , \
                    self.encoder_right , self.encoder_left , self.LDR_top , self.LDR_front , \
                    self.tempreture_sensor , self.voltage , self.current = self.incoming.split(";")
                self.time_stamp = float(self.time_stamp)
                self.Ax = float(self.Ax)
                self.Ay = float(self.Ay)
                self.Az = float(self.Az)
                self.Gx = float(self.Gx)
                self.Gy = float(self.Gy)
                self.Gz = float(self.Gz)
                self.Ultrasonic_rear_right = float(self.Ultrasonic_rear_right)
                self.Ultrasonic_right = float(self.Ultrasonic_right)
                self.Ultrasonic_front = float(self.Ultrasonic_front)
                self.Ultrasonic_left = float(self.Ultrasonic_left)
                self.Ultrasonic_rear_left = float(self.Ultrasonic_rear_left)
                self.Ultrasonic_back = float(self.Ultrasonic_back)
                self.encoder_right = float(self.encoder_right)
                self.encoder_left = float(self.encoder_left)
                self.LDR_top = float(self.LDR_top)
                self.LDR_front = float(self.LDR_front)
                self.tempreture_sensor = float(self.tempreture_sensor)
                self.voltage = float(self.voltage)
                self.current = float(self.current)
            except:
                print "eBot.read(): bad formatted data received"
                print self.incoming
            if self.offset_counter == 2:
                self.Ax_offset = self.Ax
                self.Ay_offset = self.Ay
                self.Az_offset = self.Az
                self.Gx_offset = self.Gx
                self.Gy_offset = self.Gy
                self.Gz_offset = self.Gz
            if self.offset_counter>2 and self.offset_counter<self.offset_counter_iteration:# we just average the first 50
            # readings of the accelerometer and Gyro sensor and find the offset value by averaging them
                self.Ax_offset = (self.Ax+self.Ax_offset)
                self.Ay_offset = (self.Ay+self.Ay_offset)
                self.Az_offset = (self.Az+self.Az_offset)
                self.Gx_offset = (self.Gx+self.Gx_offset)
                self.Gy_offset = (self.Gy+self.Gy_offset)
                self.Gz_offset = (self.Gz+self.Gz_offset)

            if self.offset_counter == self.offset_counter_iteration:# we just average the first 50
            # readings of the accelerometer and Gyro sensor and find the offset value by averaging them
                self.Ax_offset = self.Ax_offset/(self.offset_counter_iteration-2)
                self.Ay_offset = self.Ay_offset/(self.offset_counter_iteration-2)
                self.Az_offset = self.Az_offset/(self.offset_counter_iteration-2)
                self.Gx_offset = self.Gx_offset/(self.offset_counter_iteration-2)
                self.Gy_offset = self.Gy_offset/(self.offset_counter_iteration-2)
                self.Gz_offset = self.Gz_offset/(self.offset_counter_iteration-2)

            if self.offset_counter>self.offset_counter_iteration:
                sampling_time = (self.time_stamp-self.prev_time_stamp)/1000.
                if sampling_time>0:
                    if abs(self.Gz-self.Gz_offset)>50: # to remove the noise
                        self.heading = self.heading+sampling_time*(self.Gz-self.Gz_offset) # the integration to get the heading
                    self.heading_scaled = self.heading/130.5 #128.7
                    self.pos_values[0],self.pos_values[1],self.pos_values[2] = \
                        self.EKF.update_state([self.heading_scaled*pi/180.,self.encoder_right/1000.,self.encoder_left/1000.],sampling_time)
                    self.pos_values[2] = degrees(self.pos_values[2])
                    self.pos_values[2] = self.pos_values[2] % 360
                    if self.pos_values[2]>180:
                        self.pos_values[2]-=360
                    elif self.pos_values[2]<-180:
                        self.pos_values[2]+=360
        return self.incoming


    def recieve_background(self):
        while self.thread_flag:
            self.read()
            sleep(0.005)
        return



    def close(self):
        """
        Close BLE connection with eBot.
        """
        self.disconnect()

    #TODO: add disconnect feedback to robot
    def disconnect(self):
        """
        Close BLE connection with eBot.
        """
        #self.receive_thread.
        sleep(0.05)
        self.thread_flag = 0
        sleep(0.05)
        if self.serialReady:
            try:
                self.port.close()
                print "Successful", "eBot successfully disconnected."
            except:
                self.lostConnection()

    def robot_uS(self):
        """
        Retrieves and returns all six ultrasonic sensor values from the eBot in meters.

        :rtype: list
        :return: sonarValues
        """
        self.sonarValues[4] = float(self.Ultrasonic_rear_right) / 1000
        self.sonarValues[3] = float(self.Ultrasonic_right) / 1000
        self.sonarValues[2] = float(self.Ultrasonic_front) / 1000
        self.sonarValues[1] = float(self.Ultrasonic_left) / 1000
        self.sonarValues[0] = float(self.Ultrasonic_rear_left) / 1000
        self.sonarValues[5] = float(self.Ultrasonic_back) / 1000
        return self.sonarValues

    def calibration_values(self):
        """
        Retrieves and returns the calibration values of the eBot.

        :rtype: list
        :return: all_Values (calibration values)
        """
        if self.serialReady:
            try:
                self.port.write("2C")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        while len(values) < 10:
            if self.serialReady:
                try:
                    self.port.write("2C")
                except:
                    self.lostConnection()
            line = self.port.readline()
            values = line.split(";")
        self.all_Values[0] = float(values[0])
        self.all_Values[1] = float(values[1])
        self.all_Values[2] = float(values[2])
        self.all_Values[3] = float(values[3])
        self.all_Values[8] = float(values[4]) / 1000
        self.all_Values[7] = float(values[5]) / 1000
        self.all_Values[6] = float(values[6]) / 1000
        self.all_Values[5] = float(values[7]) / 1000
        self.all_Values[4] = float(values[8]) / 1000
        self.all_Values[9] = float(values[9]) / 1000
        return self.all_Values

    def halt(self):
        """
        Halts the eBot, turns the motors and LEDs off.
        """
        if self.serialReady:
            try:
                self.port.write("2H")
            except:
                self.lostConnection()
        sleep(0.05)

    def led(self, bool):
        """
        Controls the state of the LED on the eBot.

        :param bool: Defines whether the LED should turn ON (1) or OFF (0)
        """
        if (bool == 1):
            self.led_on()
        elif (bool == 0):
            self.led_off()
        else:
            self.led_off()
        sleep(0.05)

    def led_on(self):
        """
        Turns the LED on the eBot ON.
        """
        if self.serialReady:
            try:
                self.port.write("2L")
            except:
                self.lostConnection()
        sleep(0.05)

    def led_off(self):
        """
        Turns the LED on the eBot OFF.
        """
        if self.serialReady:
            try:
                self.port.write("2l")
            except:
                self.lostConnection()
        sleep(0.05)

    def light(self):
        """
        Retrieves and returns a list of tuples with the light index. 0 index is front and 1st index is top LDR readings.

        :rtype: list
        :return: ldrvalue: LDR Readings
        """
        self.ldrvalue[0] = float(self.LDR_front)
        self.ldrvalue[1] = float(self.LDR_top)
        return self.ldrvalue

    #Double check true vs. false
    def obstacle(self):
        """
        Tells whether or not there is an obstacle less than 250 mm away from the front of the eBot.

        :rtype: bool
        :return: True if obstacle exists
        """
        if self.Ultrasonic_front>250:
            return False
        else:
            return True


    #TODO: implement x, y, z returns and a seperate odometry function
    def acceleration(self):
        """
        Retrieves and returns accelerometer values; absolute values of X,Y and theta coordinates of robot with reference
        to starting position.

        :rtype: list
        :return: acc_values: Accelerometer values
        """
        self.acc_values[0] = float(self.Ax-self.Ax_offset)
        self.acc_values[1] = float(self.Ay-self.Ay_offset)
        self.acc_values[2] = float(self.Az-self.Az_offset)
        self.acc_values[3] = float(self.Gx-self.Gx_offset)
        self.acc_values[4] = float(self.Gy-self.Gy_offset)
        self.acc_values[5] = float(self.Gz-self.Gz_offset)
        return self.acc_values

    def position(self):
        """
        Retrieves and returns position values of the eBot.

        :rtype: list
        :return: pos_values: X,Y,Z position values
        """
        #self.pos_values[0] , self.pos_values[1] = self.EKF.get_position()
        #self.pos_values[2] = self.EKF.get_heading()
        #self.pos_values[2] = 0
        return self.pos_values[0],self.pos_values[1],self.pos_values[2]

    #TODO: implement temperature feedback from MPU6050 IC
    def temperature(self):
        """
        Retrieves and returns temperature reading from the eBot.

        :rtype: int
        :return: Temperature value.
        """

        return int(self.tempreture_sensor)

    def power(self):
        """

        :return:
        """

        self.p_value[0] = float(self.voltage)
        self.p_value[1] = float(self.current)
        return self.p_value

    def imperial_march(self):
        """

        """
        if self.serialReady:
            try:
                self.port.write("2b")
            except:
                self.lostConnection()

    def buzzer(self, btime, bfreq):
        """
        Plays the buzzer for given time at given frequency.

        :param btime: Time in Seconds
        :param bfreq: Frequency in Hertz
        """
        buzzer_time = int(btime)
        buzzer_frequency = int(bfreq)
        bt1 = str(buzzer_time)
        bf1 = str(buzzer_frequency)
        str_len = len(bt1) + len(bf1)+2
        str_len =str_len + 48
        myvalue = chr(str_len) + 'B' + bt1 + ';' + bf1
        if self.serialReady:
            try:
                self.port.write(myvalue)
            except:
                self.lostConnection()
        sleep(buzzer_time/1000)

    def port_name(self):
        """
        Returns port name of currently connected eBot.

        :return: port: Port name
        """
        return self.port


    def port_close(self):
        """
        Closes the COM port that corresponds to the eBot object.

        :raise Exception: Could not close COM port
        """
        try:
            self.port.close()
        except:
            self.serialReady = False
            raise Exception("Could not close COM port.")

    #TODO: Add com port argument functionality
    def port_open(self):
        """
        Still under development, currently just calls connect
        """
        self.connect()

    def wheels(self, LS, RS):
        """
        Controls the speed of the wheels of the robot according to the specified values
        :param LS: Speed of left motor
        :param RS: Speed of right motor
        """
        if LS > 1:
            LS = 1
        elif LS < -1:
            LS = -1
        if RS > 1:
            RS = 1
        elif RS < -1:
            RS = -1
        Left_speed = int((LS + 2) * 100)
        Right_speed = int((RS + 2) * 100)
        LS1 = str(Left_speed)
        RS1 = str(Right_speed)
        myvalue = '8' + 'w' + LS1 + ';' + RS1
        if self.serialReady:
            try:
                self.port.write(myvalue)
            except:
                self.lostConnection()

                # class ebot_f:

                # def __init__(self):
        sleep(0.05)
    def wheel_calibrate(self, LS, RS):
        """
        Controls the speed of the wheels of the robot according to the specified values
        :param LS: Speed of left motor
        :param RS: Speed of right motor
        """
        if LS > 9999:
            LS = 9999
        elif LS < 1:
            LS = 1
        if RS > 9999:
            RS = 9999
        elif RS < 1:
            RS = 1
        LS1 = str(LS).zfill(4)
        RS1 = str(RS).zfill(4)
        myvalue = ':' + 'c' + LS1 + ';' + RS1
        if self.serialReady:
            try:
                self.port.write(myvalue)
            except:
                self.lostConnection()

                # class ebot_f:

                # def __init__(self)
    def lostConnection(self):
        """
        Handler for the case that the computer loses connection with the eBot.

        :raise Exception: Robot Connection Lost
        """
        try:
            self.port.close()
        except:
            pass
        self.serialReady = False
        print "COM Error", "Robot connection lost..."
        raise Exception("Robot Connection Lost")
        ################################################################################
