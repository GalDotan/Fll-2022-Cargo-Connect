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
    x = 0 
    ev3.screen.clear()
    pic = "MA"
    while True :
            ev3.screen.draw_image(0,0,pic)
            if Button.DOWN in ev3.buttons.pressed():
                x = 1
                pic = "Green Run"
                Green_run()
            elif Button.UP in ev3.buttons.pressed():
                x = 2
                pic = "Red Run"
                Red_run()
            elif Button.LEFT in ev3.buttons.pressed():
                x = 3
                pic = "Purple Run"
                Purple_run
            elif Button.RIGHT in ev3.buttons.pressed():
                x = 4
                pic = "Gray Run"    
                Gray_run()
            elif Button.CENTER in ev3.buttons.pressed():
                Orange_run()
                    
                    
                
            




