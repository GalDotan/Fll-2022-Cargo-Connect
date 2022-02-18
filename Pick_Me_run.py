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
    ev3.screen.clear()
    while True :
            pic = "MA"
            ev3.screen.draw_image(0,0,pic)
            if Button.DOWN in ev3.buttons.pressed():
                pic = "Green Run"
                ev3.screen.draw_image(0,0,pic)
                wait(1000)
                Green_run()
            elif Button.UP in ev3.buttons.pressed():
                pic = "Red Run"
                ev3.screen.draw_image(0,0,pic)
                wait(1000)
                Red_run()
            elif Button.LEFT in ev3.buttons.pressed():
                pic = "Purple Run"
                ev3.screen.draw_image(0,0,pic)
                wait(1000)
                Purple_run()
            elif Button.RIGHT in ev3.buttons.pressed():
                pic = "Gray Run"    
                ev3.screen.draw_image(0,0,pic)
                wait(1000)
                Gray_run()
            elif Button.CENTER in ev3.buttons.pressed():
                wait(1000)
                Orange_run()
                    
                    
                
            




