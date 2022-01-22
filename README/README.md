# Fll-2022-Cargo-Connect
#Created by Gal Dotan
#Fll Team #1201
 
MicroPythone Version V2.0
 
 
Ports:
Left Drive Motor - Port B
Right Drive Motor - Port C
Left Medium Motor - Port D
Right Medium Motor - Port A
-
Color Sensor Left - Port 1
Color Sensor Right - Port 4
Gyro Sensor - Port 3
-
Robot Settings :
Linear Speed -700
Linear Acceleration -700
Turn Speed 200
Turn Acceleration 200
-
Drive Base:
LLM
RLM
Wheel Diameter 60
Axle Track 127  
-
Files:
main.py- the main program that cs code will run_angle
object_creation.py- in this program the: motors, sensors, drive base and ev3 brick are created
Driving_functions.py - in this program all of the driving functions like Gyroline_W_acceleration and Gyro_turn_left are found
Run programs- every run has separate file. This file includes all of the functions of the run as well as the run itself
 -
Functions:
-
PID_Line_Following(Kp , Ki, Kd  , PID_distance)-
Description: Line following using 1 sensor and PID controller-
Parameters: Kp , Ki , Kd , Wheel rotations to drive
-
Gyroline_W_acceleration( PID_Gyrodistance)-
Description: Driving straight using 1 gyro sensor and PID controller(inclouds acceleration)-
Parameters:  Wheel rotations to drive
-
Gyro_turn_right(Target )-
Description: Turning right using 1 gyro sensor and PID controller
Parameters:  Angle to turn
-
Gyro_turn_left(Target )-
Description: Turning left using 1 gyro sensor and PID controller
Parameters:  Angle to turn
-
Drop_model()-
Description: Dropping M01 model and food delivery-
Parameters:  None
-
Drop_box()-
Description: Dropping the home delivery to the door-
Parameters:  None
-
Arm_up()-
Description: Moving the main arm up-
Parameters:  None
-
Arm_down()-
Description: Moving the main arm down-
Parameters:  None
-
Reset_gyro()-
Description: Reset the measured angle of the gyro-
Parameters:  None
-
Reset_motores_angle()-
Description: Reset the measured angle of the drive motors-
Parameters:  None
<<<<<<< HEAD
 
=======
>>>>>>> 44bf12fa5e050991f4a57617e4dd8c7f97ad557c
 

