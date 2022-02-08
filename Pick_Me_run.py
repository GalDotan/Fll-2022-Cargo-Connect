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
from dev_mode import *

def Pick_Me():
    while True :
            if Button.DOWN in ev3.buttons.pressed():
                ev3.speaker.beep(frequency=500, duration=200)
                #Gray_run()
            elif Button.RIGHT in ev3.buttons.pressed():
                ev3.light.on(Color.GREEN)
                ev3.speaker.beep(frequency=500, duration=200)
                #Green_run()
            elif Button.UP in ev3.buttons.pressed():
                ev3.light.on(Color.RED)
                ev3.speaker.beep(frequency=500, duration=200)
                #Red_run()
            elif Button.LEFT in ev3.buttons.pressed():
                ev3.light.on(Color.ORANGEk)
                ev3.speaker.beep(frequency=500, duration=200)
                #Purple_run()    
            ev3.light.on(Color.BLUE)



