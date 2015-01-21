from time import *
import os
import sys
from serial import Serial
# import serial
import glob
from Tkinter import *
import tkMessageBox
import Tkinter

if os.name == 'nt':
    try:
        import _winreg as winreg
    except:
        pass


class eBot:
    def __init__(self):
        self.sonarValues = [0, 0, 0, 0, 0, 0]
        self.all_Values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.port = None
        self.serialReady = False
        self.ldrvalue = [0, 0]
        self.p_value = [0, 0]
        self.acc_values = [0, 0, 0, 0, 0, 0]
        self.pos_values = [0, 0, 0]

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
                ports = glob.glob('/dev/tty.eBo*')
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
        for port in ports:
            try:
                if (line[:4] == "eBot"):
                    break
                s = Serial(port, baudRate, timeout=1.0, writeTimeout=1.0)
                s._timeout = 1.0
                s._writeTimeout = 1.0
                #try:
                #    s.open()
                #except:
                #    continue

                while (line[:4] != "eBot"):
                    s.write("<<1?")
                    sleep(0.5)
                    line = s.readline()
                    if (line[:4] == "eBot"):
                        ebot_ports.append(port)
                        ebot_names.append(line)
                        connect = 1
                        self.port = s
                        self.portName = port
                        self.port._timeout = 1.0
                        self.port._writeTimeout = 1.0
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
            window = Tkinter.Tk()
            window.wm_withdraw()
            tkMessageBox.showwarning("Connection Error", "No eBot found. Please reconnect and try again.",
                                     parent=window)
            #import ctypes  # An included library with Python install.
            #ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
            raise Exception("No eBot found")

        sleep(.01)
        try:
            self.port.write('<<1E')
            sleep(0.4)
            line = self.port.readline()
            if (line != ">>1B\n" and line != ">>1B"):
                self.lostConnection()
            self.port.write("<<1O")
            sleep(0.4)
            self.port.write("F")
            sleep(0.2)
            self.port.flushInput()
            self.port.flushOutput()
        except:
            window = Tkinter.Tk()
            window.wm_withdraw()
            tkMessageBox.showerror("COM Error", "Robot connection lost...", parent=window)
            sys.stderr.write("Could not write to serial port.\n")
            self.serialReady = False
            sys.stderr.write("Robot turned off or no longer connected.\n")

        self.serialReady = True

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
        sleep(1)
        if self.serialReady:
            try:
                self.port.close()
                window = Tkinter.Tk()
                window.wm_withdraw()
                tkMessageBox.showinfo("Successful", "eBot successfully disconnected.", parent=window)
            except:
                self.lostConnection()

    def robot_uS(self):
        """
        Retrieves and returns all six ultrasonic sensor values from the eBot in meters.

        :rtype: list
        :return: sonarValues
        """
        if self.serialReady:
            try:
                self.port.write("2S")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        while len(values) < 7:
            if self.serialReady:
                try:
                    self.port.write("2S")
                except:
                    self.lostConnection()
            line = self.port.readline()
            values = line.split(";")
        self.sonarValues[4] = float(values[0]) / 1000
        self.sonarValues[3] = float(values[1]) / 1000
        self.sonarValues[2] = float(values[2]) / 1000
        self.sonarValues[1] = float(values[3]) / 1000
        self.sonarValues[0] = float(values[4]) / 1000
        self.sonarValues[5] = float(values[5]) / 1000
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

    def led_on(self):
        """
        Turns the LED on the eBot ON.
        """
        if self.serialReady:
            try:
                self.port.write("2L")
            except:
                self.lostConnection()

    def led_off(self):
        """
        Turns the LED on the eBot OFF.
        """
        if self.serialReady:
            try:
                self.port.write("2l")
            except:
                self.lostConnection()

    def light(self):
        """
        Retrieves and returns a list of tuples with the light index. 0 index is front and 1st index is top LDR readings.

        :rtype: list
        :return: ldrvalue: LDR Readings
        """
        if self.serialReady:
            try:
                self.port.write("2D")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        self.ldrvalue[0] = float(values[0])
        self.ldrvalue[1] = float(values[1])
        return self.ldrvalue

    #Double check true vs. false
    def obstacle(self):
        """
        Tells whether or not there is an obstacle less than 250 mm away from the front of the eBot.

        :rtype: bool
        :return: True if obstacle exists
        """
        if self.serialReady:
            try:
                self.port.write("2O")
            except:
                self.lostConnection()
        line = self.port.readline()
        return bool(int(line[0]))

    #        return bool(line[0])

    #TODO: implement x, y, z returns and a seperate odometry function
    def acceleration(self):
        """
        Retrieves and returns accelerometer values; absolute values of X,Y and theta coordinates of robot with reference
        to starting position.

        :rtype: list
        :return: acc_values: Accelerometer values
        """
        if self.serialReady:
            try:
                self.port.write("2A")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        self.acc_values[0] = float(values[0])
        self.acc_values[1] = float(values[1])
        self.acc_values[2] = float(values[2])
        self.acc_values[3] = float(values[3])
        self.acc_values[4] = float(values[4])
        self.acc_values[5] = float(values[5])
        return self.acc_values

    def position(self):
        """
        Retrieves and returns position values of the eBot.

        :rtype: list
        :return: pos_values: X,Y,Z position values
        """
        if self.serialReady:
            try:
                self.port.write("2P")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        self.pos_values[0] = float(values[0])
        self.pos_values[1] = float(values[1])
        self.pos_values[2] = float(values[2])
        return self.pos_values

    #TODO: implement temperature feedback from MPU6050 IC
    def temperature(self):
        """
        Retrieves and returns temperature reading from the eBot.

        :rtype: int
        :return: Temperature value.
        """
        if self.serialReady:
            try:
                self.port.write("2T")
            except:
                self.lostConnection()
        line = self.port.readline()
        t_value = line.split(";")
        if len(t_value) < 2:
            return 0
        else:
            return int(t_value[0])

    def power(self):
        """

        :return:
        """
        if self.serialReady:
            try:
                self.port.write("2V")
            except:
                self.lostConnection()
        line = self.port.readline()
        t_values = line.split(";")
        self.p_value[0] = float(t_values[0])
        self.p_value[1] = float(t_values[1])
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
        window = Tkinter.Tk()
        window.wm_withdraw()
        tkMessageBox.showerror("COM Error", "Robot connection lost...", parent=window)
        raise Exception("Robot Connection Lost")
        ################################################################################
