eBot-API
========


APIs to interface with eBots

TOP view, with eBot upright
LED positions
left- Bluetooth
Centre- Charging
Right-MCU
---
title: Getting started with eBot 
description: eBot hardware and Soar code
author: Abhishek Gupta, Harsh Bhatt
tags: eBot, Soar, Edgebotix
created:  2014 Oct 20
modified: 2014 Nov 19

---

Getting Started with eBot
=========

## eBot Description

[![solarized dualmode](https://github.com/altercation/solarized/raw/master/img/solarized-yinyang.png)](#features)

eBots are a robust, 3D-printed versatile STEM learning robotics platform that provide modularity and customization options. eBots aim to bridge the link between theory and practice by providing the ideal platform for students to collaborate and use their combined knowledge to build the best solution to a task. EdgeBotix wants to build the best supporting community and provide resources for teaching, making it extremely easy to integrate into the curriculum, something not seen in current educational robots.  

### Technical Specification

The following are detailed technical specifications of the eBots:
*	**Physical robot**
    *	15 x 15 x 8 cm, ABS plastic housing with various colour options
    *	Tank drive (2 drive treads)
        *	Powered by 2 low current Tamiya DC brushed motors
        *	150 RPM no load speed
        *	.2 m/s average speed
*	**Firmware**
    *	Powered by an ARM Cortex M0 microprocessor running at 48 MHz
*	**Sensors & other I/O**
    *	6 Sonar range finders (15 cm to 3 m range)
        *	1 Front facing
        *	2 At 45° from front
        *	2 Side facing
        *	1 Back facing
        *	Within 20 cm dead zone requirement
    *	6 DOF IMU (Accelerometer & Gyroscope)
        *	Raw acceleration data in x, y and z axis
        *	Raw euler angle (rotation) along x, y and z axis
    *	2 Encoders, providing distance and velocity measurements for both treads
    *	2 LDRs
        *	1 Top facing
        *	1 Front facing
    *	Onboard buzzer with a frequency range of 100 Hz to 10 KHz
*	**Wireless communication**
    *	Bluetooth connectivity to host computer
        *	Each robot has unique serialized Bluetooth identifier, in accordance to the serial number labeled on robot body
*	**Power**
    *	2 Ah Li-Po battery providing 3+ hours of continuous runtime
    *	Mini USB charging port
        *	1 Hour full charge time
*	**Software**
    *	eOS Running onboard eBots (an RTOS built on the mbed RTOS)
*	**Interface**
    * Currently there are two interface with python language
        *   [Soar Interface](#soar) 
        *   [API interface](#features)

### Pairing eBot
* eBot could be paired by entering the pairing code "0000". If you want the step by step guide of pairing with your system you can click [here](#detailed pairing).

### Python Installation
You might need:
* [Python 2.7](http://epd-free.enthought.com/?Download=Download+EPD+Free+7.3-2) 

Soar
---------
This section assumes that you have Python 2.7 already installed. 
To install Digital World Library, follow the steps according to your platform:
1.	OS X and Linux:
   * Download SOAR-master.zip from the [github](https://github.com/EdgeBotix/SOAR)
   * Open Terminal
   * Go the directory/folder where you save the file, e.g. if you save it to Mac's default Downloads folder, then type :
```
    cd $HOME/Downloads
```
   * Unzip the file, e.g. type :
```
    tar SOAR-master.zip
```
   * Go to the SOAR-master folder, e.g. type:
```    
   cd SOAR-master
```
   * Install the library by typing:
```   
   sudo python setup.py install
```
2.	Windows:
    * Download SOAR-master.zip from the [github](https://github.com/EdgeBotix/SOAR)
   * Unzip the file
   * Open Command Prompt by typing "cmd" from the Start Menu
   * Go the directory/folder where you have unzipped the file, e.g. type :
``` 
    cd C:\Downloads\SOAR-master\
``` 
   * Install the library by typing:
``` 
   python setup.py install
``` 

### RUNNING SIMULATOR - SOAR
After you have installed the Digital World Library, you can run the
simulator, called SOAR. To run it, follow the steps below:
1. OS X and Linux:
   * Open Terminal
   * Go to the SOAR-master folder
   * Go to soar folder
   * Run soar by typing: 
``` 
	python runsoar.py
``` 

2. Windows:
    * Open Command Prompt by typing "cmd" from the Start Menu
    * Go to the folder where you store Digital World Library, e.g.:
``` 
    cd C:\Downloads\SOAR-master\
```
* Go to "soar" folder:
```
   cd soar
```
* Run soar by typing:
```
    python runsoar.py
```

### USING SIMULATOR - SOAR

1. Running the code and connect to eBot using wireless connection:
   * Run Soar 
   * Click "Simulator" button to load any Python files for the Worlds
   * Click "Brain" button and choose the Python files containing your robot brain
   * Click "START" button to start connection with EBot

WORLD

Some World files for simulation has been created ans it is part of the Digital Library Package. It is also included in this package under the folder "worlds".

BRAIN

A simple Brain file has been included: brainfile.py.
