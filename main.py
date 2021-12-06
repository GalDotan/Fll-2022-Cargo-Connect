#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.




from core_funcsions import *

ev3.speaker.beep(500, 3000)

def First_Run():
    #Gyro_Stright(1)
    #Gyro_Turn_Left(28)
    #Gyro_Stright(2.1)
    #Gyro_Turn_Right(-33)
    #Gyro_Stright(2)
    #LMM.run(1000)
    #wait(10)
    #LMM.stop()
    Gyro_Stright(2)

First_Run()

