#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Object_creation import *
from Green_run import *
from Red_run import *
from Gray_run import *
from Purple_run import *
from Orange_run import *
from Driving_functions import *
from Pick_Me_run import *


ev3.screen.clear()
ev3.screen.draw_text(50, 30, "MA1201", text_color=Color.BLACK, background_color=None)
wait(100000)
#MA1201 = Image(ImageFile.MA1201)

#ev3.screen.load_image(MA1201)



