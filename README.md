# Fll-2022-Cargo-Connect
#Created by Gal Dotan
#Fll Team #1201

MicroPythone Version V2.0


Ports:
Left Drive Motor - Port B
Right Drice Motor - Port C
Left Medium Motor - Port D
Right Medium Motor - Port A
-
Color Sensore Left - Port 1
Color Sensore Right - Port 4
Gyro Sensore - Port 3
-
Robot Seetings :
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

Functions:
-
PID_Line_Following(Kp , Ki, Kd  , PID_distance)-
Description: Line following using 1 sensore and PID controller-
Parameters: Kp , Ki , Kd , Wheel rotations to drive
-
Gyro_Straight( PID_Gyrodistance)-
Description: Driving straight using 1 gyro sensore and POD controller-
Parameters:  Wheel rotations to drive
-
Gyro_turn_right(Target )-
Description: Turning right using 1 gyro sensore and PID controler-
Parameters:  Angle to turn
-
Gyro_turn_left(Target )-
Description: Turning left using 1 gyro sensore and PID controler-
Parameters:  Angle to turn
-
Drop_model()-
Description: Droping M01 model and food delivery-
Parameters:  None
-
Drop_box()-
Description: Droping the home delivery to the door-
Parameters:  None
-
Arm_up()-
Description: Moing the main arm up-
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
Description: Reset the measured angle of the motore-
Parameters:  None
<<<<<<< HEAD

=======
>>>>>>> 44bf12fa5e050991f4a57617e4dd8c7f97ad557c
