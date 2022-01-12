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
# Importing files:
from core_funcsions import *



def Red_run():
    Reset_gyro()
    Gyro_Straight(1.1,0)
    Gyro_turn_right (90)
    robot.straight(170)
    Gyro_Straight(5.6,90)
    robot.straight(160)
    Gyro_Straight(1.4,90)
    Gyro_turn_left(0)
    robot.straight(400)
    Reset_gyro()
    Drop_box()
    Gyro_Straight(2,0)
    Gyro_turn_right(95)
    Gyro_Straight(0.3,95)
    Drop_model()
    Arm_up()
    Gyro_Straight(1.3,95)
    Arm_down()
    wait(150)
    robot.straight(100)
    Gyro_turn_left(0)
    Gyro_Straight(2.3, 0)
    Gyro_turn_right(90)
    Gyro_Straight(0.55, 90)
    robot.straight(100)
    Gyro_turn_right(180)
    robot.straight(400)
    Reset_gyro()
    Gyro_Straight(2, 0)
    Gyro_turn_right(90)
    Gyro_Straight(1.8,90)
    Gyro_turn_right(215)
    Gyro_turn_left(90)
    Gyro_Straight(6,55)

def Green_run():
    Reset_gyro()

def Gray_run():
    Reset_gyro()

def Orange_run():
    Reset_gyro()

def Purple_run():
    Reset_gyro()



