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


# Create your objects here.
ev3 = EV3Brick()
LLM = Motor(Port.B)
RLM = Motor(Port.C)
RMM = Motor (Port.D)
LMM = Motor (Port.A)
Gyrogirl = GyroSensor(Port.S3)
Colorboy_left = ColorSensor(Port.S1)
Colorgirl_right = ColorSensor(Port.S4)
robot = DriveBase(LLM, RLM, wheel_diameter=60, axle_track=127)
robot.settings(-1000,-1000, 200, 200)


def PID_Line_Following(Kp , Ki, Kd  , PID_distance):
    ev3.speaker.beep()
    degres = PID_distance*-360
    Target = 0
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = -150  
    KP = 0
    KI = 0
    KD = 0
    Kp = 0.38
    Ki = 1.3
    Kd = 0.005
    ev3.speaker.beep()
    while RLM.angle() >= degres:
        Error = Target-Colorboy_left.reflection() 
        KP = Error*Kp 
        Intgral = Intgral+Error*0.001
        KI = Intgral*Ki 
        Derivative = Error-Last_Error 
        Last_Error = Error
        KD = Derivative*Kd 
        Turn_Rate = KP+KD+KI
        Nag_Turn_Rate = Turn_Rate*-1
        robot.drive(Drive_Speed , Nag_Turn_Rate )
        wait(1)
    robot.stop()
    ev3.speaker.beep()
#Line following using 1 sensore and PID controller
def Gyro_Straight(PID_Gyrodistance):
    ev3.speaker.beep()
    degres = PID_Gyrodistance*-360
    Target = 0
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = -230 
    KP = 0
    KI = 0
    KD = 0
    Kp = 2.8
    Ki = 1.5
    Kd = 0.005
    Gyrogirl.reset_angle(0)
    while RLM.angle() >= degres:
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
    ev3.speaker.beep()
#Driving straight using 1 gyro sensore and POD controller
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
    Gyrogirl.reset_angle(0)
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
        robot.drive(Drive_Speed , Nag_Turn_Rate )
        wait(1)
    robot.stop()
    ev3.speaker.beep()
#Turning right using 1 gyro sensore and PID controler
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
    Gyrogirl.reset_angle(0)
    while Gyrogirl.angle() <= Target:
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
    ev3.speaker.beep()
#Turning left using 1 gyro sensore and PID controler
def Drop_model():
    RMM.run_angle(-1000, 70)
    wait(100)
    RMM.run_angle(-1000, -70)
#Droping M01 model and food delivery
def Drop_box():
    LMM.run_angle(-100000, 180)
    wait(150)
    LMM.run_angle(-100000, -180)
 #   
#Droping the home delivery to the door
def Arm_up():
    RMM.run_angle(-1000, 70)
#Moing the main arm up
def Arm_down():
    RMM.run_angle(-1000, -70)
#Moving main arm down  

