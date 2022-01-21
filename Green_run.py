from Object_creation import *

def Green_Arm_down():  
    RMM.run_target(-1000,1500 )
#Moving main arm down  
def Green_Arm_up():
    RMM.run_target(-1000,0 )    
#Moing the main arm up
def Green_Arm_dwn():
    RMM.run_target(-1000, 1420)
#Moving main arm almost down 
def Green_run():
    Reset_gyro()
    Reset_motores_angle(0)
    ev3.speaker.beep()
    Green_Arm_dwn()
    d_speed(200, 2, 0)
    Gyro_turn_left(-70)
    Gyro_turn_right(0)
    d_speed(200, 1, 0)
    Gyro_turn_right(40)
    d_speed(200, 1.1, 0)
    Gyro_turn_right(55)
    d_speed(200, 0.14 ,55)
    Green_Arm_up()
    robot.drive(250, 15)
    ev3.speaker.beep()
    Gyro_turn_left(-50)