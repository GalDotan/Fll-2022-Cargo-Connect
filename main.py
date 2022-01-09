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
#importing files
from core_funcsions import *



Gyro_Straight(1.2)
wait(2)
Gyro_turn_right (90)
wait(2)
Gyro_Straight(5.2)
wait(2)
robot.straight(60)
wait(3)
Gyro_Straight(1)
wait(1)
robot.straight(60)