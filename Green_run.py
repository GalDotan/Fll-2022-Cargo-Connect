#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Object_creation import *
from Driving_functions import *


def Green_Arm_down():  
    RMM.run_target(-1000,1500 )
#Moving main arm down  
def Green_Arm_up():
    RMM.run_target(-1000,0 )    
#Moving the main arm up
def Green_Arm_dwn():
    RMM.run_target(-1000, 1420)
#Moving main arm almost down 
def Green_run():
    Reset_gyro()
    RMM.reset_angle(0)
    ev3.speaker.beep()
    Green_Arm_dwn()
    Gyroline_W_acceleration(200, 2.2, 0)
    Gyro_turn_left(-70)
    Gyro_turn_right(0)
    Gyroline_W_acceleration(200, 1, 0)
    Gyro_turn_right(40)
    Gyroline_W_acceleration(200, 1.4, 40)
    Gyro_turn_right(55)
    Gyroline_W_acceleration(200, 0.31 ,55)
    Green_Arm_up()
    ev3.speaker.beep()
    Gyro_turn_left(-50)
    robot.straight(90)
    Gyro_turn_left(-30)