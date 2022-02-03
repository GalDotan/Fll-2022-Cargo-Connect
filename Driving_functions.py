#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Object_creation import *

def Gyrolineb_W_acceleration(max_speed, PID_Gyrodistance, Target):
    watch = StopWatch()
    watch.reset()
    robot.stop()
    RLM.reset_angle(0)
    degrees = PID_Gyrodistance*360
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Drive_Speed = 0
    Nag_Turn_Rate = 0
    KP = 0  
    KI = 0
    KD = 0
    Kp = 1.7
    Ki = 1.3
    Kd = 0.005
    while RLM.angle() <= degrees:
        Ct = watch.time()
        max_v = max_speed / 300 * 1
        V_Speed = Ct * max_v
        print("Vspeed is ",V_Speed)
        print("Max speed is ",max_speed)
        if V_Speed >= max_speed :
            Drive_Speed = max_speed
        else:
            Drive_Speed = V_Speed
        print("Drive speed is is ",Drive_Speed)
        Error = Target-Gyrogirl.angle() 
        KP = Error*Kp
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*1
        robot.drive(Drive_Speed , Nag_Turn_Rate ) 
        wait(1)
    robot.stop()
    RLM.reset_angle(0)

def Gyroline_W_acceleration(max_speed, PID_Gyrodistance, Target):
    watch = StopWatch()
    watch.reset()
    degrees = PID_Gyrodistance*-360
    robot.stop()
    RLM.reset_angle(0)
    degrees = PID_Gyrodistance*-360
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Drive_Speed = 0
    Nag_Turn_Rate = 0
    KP = 0  
    KI = 0
    KD = 0
    Kp = 1.7
    Ki = 1.3
    Kd = 0.005
    while RLM.angle() >= degrees:
        Ct = watch.time()
        max_v = max_speed / 300 * -1
        V_Speed = Ct * max_v
        max_speed_P = max_speed*-1
        if V_Speed <= max_speed_P :
            Drive_Speed = max_speed_P
        else:
            Drive_Speed = V_Speed
        Error = Target-Gyrogirl.angle() 
        KP = Error*Kp
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*1
        robot.drive(Drive_Speed , Nag_Turn_Rate ) 
        wait(1)
    robot.stop()
    RLM.reset_angle(0)

def Reset_gyro():
    Gyrogirl.reset_angle(0)

def Gyro_Straight(PID_Gyrodistance, Target,):
    robot.stop()
    RLM.reset_angle(0)
    degrees = PID_Gyrodistance*-360
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = V_Speed
    KP = 0
    KI = 0
    KD = 0
    kp = 3
    Ki = 0
    Kd = 0
    while RLM.angle() >= degrees:
        Error = Target-Gyrogirl.angle()
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*1
        robot.drive(Drive_Speed , Nag_Turn_Rate )
        wait(1)
    robot.stop()
    RLM.reset_angle(0)

def Gyro_turn_left(Target):
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = 0
    KP = 0
    KI = 0
    KD = 0
    Kp = 2.8
    Ki = 1.5
    Kd = 0.005
    while Gyrogirl.angle() >= Target:
        Error = Target-Gyrogirl.angle() 
        KP = Error*Kp 
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*1
        robot.drive(0, Nag_Turn_Rate )
        wait(1)
    robot.stop()

def Gyro_turn_right(Target):
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = 0
    KP = 0
    KI = 0
    KD = 0
    Kp = 2.8
    Ki = 1.5
    Kd = 0.005
    while Gyrogirl.angle() <= Target:
        Error = Target-Gyrogirl.angle()
        Kp = Error*Kp 
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*1
        robot.drive(Drive_Speed , Nag_Turn_Rate )
        wait(1)
    robot.stop()

def Reset_motors_angle(anglee):
    robot.stop()
    RLM.reset_angle(anglee)
    LLM.reset_angle(anglee)
    