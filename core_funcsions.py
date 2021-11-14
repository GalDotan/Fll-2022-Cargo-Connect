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
Gyroboy = GyroSensor(Port.S2)
Gyrogirl = GyroSensor(Port.S3)
Colorboy_left = ColorSensor(Port.S1)
Colorgirl_right = ColorSensor(Port.S4)
robot = DriveBase(LLM, RLM, wheel_diameter=60.2, axle_track=180.5)
robot.settings(-1000,-1000, 200, 200)





def Line_Following(distance):
    ev3.speaker.beep()
    angles = distance*-360 
    BLACK = 4
    WHITE = 45
    DRIVE_SPEED = -100
    PROPORTIONAL_GAIN = 1
    threshold = (BLACK + WHITE) / 2
    LLM.reset_angle(0)
    while LLM.angle() >= angles:
        deviation = Colorboy_left.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()
    robot.stop()
 

 

def Gyro_Stright(distance_gyro):
    ev3.speaker.beep()
    degres = distance_gyro*-360
    Gyroboy.reset_angle(0)
    reset()
    while LLM.angle() >= degres:
        correction = (0 - Gyroboy.angle())*2.5
        robot.drive(-250,correction)
    ev3.speaker.beep()
    robot.stop
    




def PID_Line_Following(PID_distance):
    ev3.speaker.beep()
    #degres = PID_distance*-360
    Target = 42
    Error = 0
    Intgral = 0
    Last_Error = 0
    Derivative = 0
    Turn_Rate = 0
    Drive_Speed = -100
    KP = 0
    KI = 0
    KD = 0
    Kp = 1.2
    Ki = 0
    Kd = 0
    while True:
        Target-Colorboy_left.reflection() = Error
        Intgral+Error = Intgral
        Error-Last_Error = Derivative
        Error*Kp = KP 
        Intgral*Ki = KI
        Derivative*Kd = KD
        KP+KI+KD = Turn_Rate
        robot.drive(Drive_Speed , Turn_Rate)
        Last_Error = Error
    robot.stop()
    ev3.speaker.beep()
        
