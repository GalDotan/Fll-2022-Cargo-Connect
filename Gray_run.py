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


def Gray_run():
    Reset_gyro()
    Gyroline_f(400, 2.1 , 0 )
    Gyroline_f(200,0.1,0)
    Gyroline_b(200, 0.3, 0)
    Gyroline_b(400, 1.8 , 90)