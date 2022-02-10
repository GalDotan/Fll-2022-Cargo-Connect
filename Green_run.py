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
    RMM.run_target(-1000,00 )
#Moving main arm down  
def Green_Arm_up():
    RMM.run_target(-1000,-1500 )    
#Moving the main arm up
def Green_Arm_dwn():
    RMM.run_target(-1000,-120)
#Moving main arm almost down 
def Green_run():
    Reset_gyro()
    RMM.reset_angle(0)
    Green_Arm_dwn()
    ev3.speaker.beep()
    Gyroline_f(200, 3.2, 0)
    Gyro_turn_right(26)
    Gyroline_f(200, 0.89, 26)
    ev3.speaker.beep()
    Gyro_turn_right(57)
    Gyroline_f(200, 0.31 ,57)
    Green_Arm_up()
    ev3.speaker.beep()                                                                          
    Gyroline_b(600, 4 , 45) 
    #Gyro_turn_left(-50)
    #Gyroline_b(20,90,-50)
    #Gyro_turn_left(-30) 
    # Above this is the code for the green helicopter thingy, do not enable for now.
    