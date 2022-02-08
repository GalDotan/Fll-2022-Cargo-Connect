#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Object_creation import *
from Object_creation import *
from Driving_functions import *

def dev_mode():
    Bat_V = ev3.battery.voltage()
    Bat_A = ev3.battery.current()
    print("Battery voltage is ",Bat_V)
    print("Battery current is ",Bat_A)
    
