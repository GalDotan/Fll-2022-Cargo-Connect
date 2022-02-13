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

def Purple_run():
    Reset_gyro()
    Gyroline_f(200, 4 , 0)
    wait(5)
    Gyroline_b(200, 4 , 0)