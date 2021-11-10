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
    #angles = distance x  360 #converting rotations to degres
    BLACK = 4
    WHITE = 46
    DRIVE_SPEED = -250
    PROPORTIONAL_GAIN = 1.2
    threshold = (BLACK + WHITE) / 2
    LLM.reset_angle(0)
    while LLM.angle() >= 1000:
        deviation = Colorboy_left.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()
    robot.stop
    LLM.Brake()
    RLM.Brake()




def Gyro_Stright(distance_gyro):
    ev3.speaker.beep()
    Gyroboy.reset_angle(0)
    reset()
    while robot.distance >= distance_gyro:
        correction = (0 - Gyroboy.angle())*2.5
        robot.drive(-250,correction)
    ev3.speaker.beep()
    robot.stop
    LLM.Brake()
    RLM.Brake()






