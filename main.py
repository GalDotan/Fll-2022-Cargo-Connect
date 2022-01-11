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



def Long_run():
    Reset_gyro()
    Gyro_Straight(1.2,0)
    wait(1)
    Gyro_turn_right (90)
    wait(1)
    robot.straight(170)
    wait(1)
    Gyro_Straight(5.6,90)
    wait(1)
    robot.straight(160)
    wait(1)
    Gyro_Straight(1.4,90)
    wait(1)
    Gyro_turn_left(0)
    wait(1)
    robot.straight(400)
    Reset_gyro()
    Drop_box()
    Gyro_Straight(2,0)
    Gyro_turn_right(95)
    Gyro_Straight(0.3,95)
    Drop_model()
    Arm_up()
    Gyro_Straight(1.2,95)
    Arm_down()
    robot.straight(100)
    wait(1)
    Gyro_turn_left(0)





ev3.speaker.beep()
ev3.speaker.beep()
wait(1000)
Long_run()
