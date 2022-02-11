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



def Pick_Me():
    x=0
    ev3.screen.clear()
    while True :
            ev3.screen.draw_image(0,0,pic)
            if Button.DOWN in ev3.buttons.pressed():
                x=1
                pic = ""
            elif Button.UP in ev3.buttons.pressed():
                x=2
                pic = ""
            elif button.LEFT in ev3.buttons.pressed():
                x=3
                pic = ""
            elif button.RIGHT in ev3.buttons.pressed():
                x=4
                pic = ""
            elif button.CENTER in ev3.buttons.pressed():
                if x == 1 :
                    Green_run()
                elif x == 2 :
                    Red_run()
                elif x == 3 :
                    Gray_run()               
                elif x == 4 :
                    Purple_run()
                    
                
            




