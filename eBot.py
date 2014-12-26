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
        self.port = None
        self.serialReady = False

    def destroy(self):
        self.disconnect()
        self.sonarValues = None
        self.port = None
        self.serialReady = None

    def getOpenPorts(self):
        """
            This Function Returns a list of tuples with the port number and its description. Used for Windows only
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
        self.connect()

    def connect(self):
        baudRate = 115200
        ports = []
        if os.name == "posix":
            if sys.platform == "linux2":
                #usbSerial = glob.glob('/dev/ttyUSB*')
                print "Support for this OS is under development."
            elif sys.platform == "darwin":
                ports = glob.glob('/dev/tty.eBot*')
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
        for port in ports:
            try:
                s = Serial(port, baudRate, timeout=1.0, writeTimeout=1.0)
                s._timeout = 1.0
                s._writeTimeout = 1.0
                #try:
                #    s.open()
                #except:
                #    continue
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
            self.port.write("EEEO")
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
        self.disconnect()

    #TODO: add disconnect feedback to robot
    def disconnect(self):
        self.halt()
        if self.serialReady:
            try:
                self.port.close()
                window = Tkinter.Tk()
                window.wm_withdraw()
                tkMessageBox.showinfo("Successful", "eBot successfully disconnected.", parent=window)
            except:
                self.lostConnection()

    def robot_uS(self):
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

    def halt(self):
        if self.serialReady:
            try:
                self.port.write("2H")
            except:
                self.lostConnection()
        self.led_off()

    def led(self, bool):
        if (bool == 1):
            self.led_on()
        elif (bool == 0):
            self.led_off()
        else:
            self.led_off()

    def led_on(self):
        if self.serialReady:
            try:
                self.port.write("2L")
            except:
                self.lostConnection()

    def led_off(self):
        if self.serialReady:
            try:
                self.port.write("2l")
            except:
                self.lostConnection()

    def light(self):
        """
            This function returns a list of tuples with the light index. 0 index is front and 1st index is top LDR readings
        """
        if self.serialReady:
            try:
                self.port.write("2D")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        float(values[0])
        float(values[1])
        return values

    #Double check true vs. false
    def obstacle(self):
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
        if self.serialReady:
            try:
                self.port.write("2A")
            except:
                self.lostConnection()
        line = self.port.readline()
        values = line.split(";")
        float(values[0])
        float(values[1])
        float(values[2])
        return values

    #TODO: implement temperature feedback from MPU6050 IC
    def temperature(self):
        if self.serialReady:
            try:
                self.port.write("2T")
            except:
                self.lostConnection()
        line = self.port.readline()
        return line
    def imeprial_march(self):
        if self.serialReady:
            try:
                self.port.write("2b")
            except:
                self.lostConnection()
    def buzzer(self, btime, bfreq):
        buzzer_time = int(btime)
        buzzer_frequency = int(bfreq)
        bt1 = str(buzzer_time)
        bf1 = str(buzzer_frequency)
        myvalue = '9' + 'B' + bt1 + ';' + bf1
        if self.serialReady:
            try:
                self.port.write(myvalue)
            except:
                self.lostConnection()

    def port_name(self):
        return self.port


    def port_close(self):
        try:
            self.port.close()
        except:
            self.serialReady = False
            raise Exception("Could not close COM port.")

    #TODO: Add com port argument functionality
    #Still under development, currently just calls connect
    def port_open(self):
        self.connect()

    def wheels(self, LS, RS):
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
