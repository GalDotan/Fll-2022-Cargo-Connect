#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
LLM = Motor(Port.B)
RLM = Motor(Port.C)
RMM = Motor (Port.D)
LMM = Motor (Port.A)
Gyrogirl = GyroSensor(Port.S3)
#Colorboy_left = ColorSensor(Port.S1)
#Colorgirl_right = ColorSensor(Port.S4)
robot = DriveBase(LLM, RLM, wheel_diameter=60, axle_track=127)
robot.settings(-400, -400, 150, 150)
