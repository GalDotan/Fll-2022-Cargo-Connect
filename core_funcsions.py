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
#Colorboy_left = ColorSensor(Port.S1)
#Colorgirl_right = ColorSensor(Port.S4)
robot = DriveBase(LLM, RLM, wheel_diameter=60, axle_track=127)
robot.settings(-700, -700, 150, 150)


def Reset_motores_angle():
    robot.stop()
    RLM.reset_angle(0)
    LLM.reset_angle(0)
#reset motore angle
def Reset_gyro():
    Gyrogirl.reset_angle(0)
#reset gyroes
def Gyro_Straight(PID_Gyrodistance, Target):
    robot.stop()
    RLM.reset_angle(0)
    degres = PID_Gyrodistance*-360
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Nag_Turn_Rate = 0
    Drive_Speed = -250 
    KP = 0
    KI = 0
    KD = 0
    Kp = 2.8
    Ki = 1.3
    Kd = 0.005
    while RLM.angle() >= degres:
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
#Turning left using 1 gyro sensore and PID controler




#Red drees
def Red_Drop_model():
    RMM.run_angle(-140, 70)
    wait(100)
    RMM.run_angle(-140, -70)
#Droping M01 model and food delivery
def Rae_Drop_box():
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



#Green drees
#Droping M01 model and food delivery
def Green_Arm_down():
    LMM.run_angle(-100000, 500)
    
def Green_Arm_up():
    LMM.run_angle(-100000, -500)

def Green_Arm_dwn():
    LMM.run_angle(-100000, 100)
    
  




