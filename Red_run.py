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

def Red_Drop_model():
    RMM.run_angle(-140, 70)

#Droping M01 model and food delivery
def Red_Drop_box():
    LMM.run_angle(-100000, 180)
    wait(150)
    LMM.run_angle(-100000, -180)
 #   
#Droping the home delivery to the door
def Red_Arm_up():
    RMM.run_angle(-1000, 70)
#Moing the main arm up
def Red_Arm_down():
    RMM.run_angle(-1000, -70)
#Moving main arm down 
def Red_run():
    RMM.reset_angle(0)
    RLM.reset_angle(0)
    Reset_gyro()
    Gyroline_f(200,1.5,0)
    Gyro_turn_right (90)
    robot.straight(170)
    Gyroline_f(200,5.6,90)
    robot.straight(160)
    Gyroline_f(200,1.5,90)
    Gyro_turn_left(0)
    robot.straight(400)
    Reset_gyro()
    Red_Drop_box()
    Gyroline_f(200,2.1,0)
    Gyro_turn_right(90)
    Gyroline_f(200,0.3,95)
    Red_Drop_model()
    wait(100)
    Gyroline_f(200,1.45,95)
    Red_Arm_down()
    wait(150)
    robot.straight(80)
    Gyro_turn_left(0)
    Gyroline_f(200,2.5, 0)
    Gyro_turn_right(87)
    Gyroline_f(200,0.55, 90)
    robot.straight(100)
    Gyro_turn_right(180)
    robot.straight(400)
    Reset_gyro()
    Gyroline_f(200,2, 0)
    Gyro_turn_right(90)
    Gyroline_f(200,2,90)
    Gyro_turn_right(215)
    Gyro_turn_left(90)
    Gyroline_f(200,6.5,55)
    