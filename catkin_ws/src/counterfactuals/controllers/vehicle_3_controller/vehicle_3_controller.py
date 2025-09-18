import math
from vehicle import Driver
from controller import Radar
import rospy
from std_msgs.msg import Bool, Float64, Empty
from geometry_msgs.msg import Pose2D

SM_INIT = 0
SM_TURN_RIGHT_1 = 10
SM_TURN_RIGHT_2 = 20
SM_CRUISE = 30
MAX_STEERING = 0.5

def calculate_turning_steering(w, L, v):
    # Steering is calculated from the kinematic model:  w = (v sin(d)) / L where:
    # v = current vehicle speed
    # w = desired angular speed
    # L = distance axis to axis
    if v == 0:
        return 0
    k = L * w / v

    if k > 0.5:
        k = 0.5
    if k < -0.5:
        k = -0.5

    steering = math.asin(k)
    if steering > MAX_STEERING: 
       print("Setting steering to ", MAX_STEERING)
       steering = MAX_STEERING
    elif steering < -MAX_STEERING:
       print("Setting steering to ", MAX_STEERING)
       steering = -MAX_STEERING       
 
    return steering


global current_x, current_y, current_a
global speed_v3
global max_speed      

# Cruise speed cars in left lane
def callback_speed_v3(msg):
    global speed_v3
    speed_cars_v3 = msg.data

def callback_current_v3_pose(msg):
    global current_x, current_y, current_a
    current_x = msg.x
    current_y = msg.y
    current_a = msg.theta

current_x = 0.0 
current_y = 0.0  
current_a = 0.0 
speed_v3 = 10
max_speed = 30 

# Initialize driver and ROS node
driver = Driver()
TIME_STEP = int(driver.getBasicTimeStep())
rospy.init_node('vehicle_3_controller', anonymous=True)
rate = rospy.Rate(1000/TIME_STEP)

# Access radar device
# Sms UMRR 0a29: Max radar range= 160.0 horiz_radar_fov= 0.628 vertical_radar_fov= 0.14
frontal_radar_Webots = Radar('Sms UMRR 0a29')
frontal_radar_Webots.enable(TIME_STEP)

rospy.Subscriber("/speed_cars_left_lane", Float64, callback_speed_v3)
rospy.Subscriber("/car_3_pose", Pose2D, callback_current_v3_pose)

# Create ROS publisher for radar data
pub_radar_scan = rospy.Publisher('/vehicle_3/v3_free_N', Bool, queue_size=10)

min_radar_range = frontal_radar_Webots.getMinRange()
max_radar_range = frontal_radar_Webots.getMaxRange()  
horiz_radar_fov = frontal_radar_Webots.getHorizontalFov()
vertical_radar_fov = frontal_radar_Webots.getVerticalFov()  
print("Obstacle Min radar range=", min_radar_range, "Obstacle Max radar range=", max_radar_range, "Obstacle horiz_radar_fov=", horiz_radar_fov, "Obstacle vertical_radar_fov=", vertical_radar_fov, sep=" ", flush=True)

valid_dist = 25 # distance to a vehicle in front that poses a potential crash
fov = math.atan2(3, valid_dist)
v3_free_N = True
msg_vehicle_3_pose = Pose2D()

#radar_returns = [r for r in radar_returns if r.range != 1.0]
#AttributeError: 'RadarTarget' object has no attribute 'range'

# Pause policy.py a little bit
rate = rospy.Rate(1) # Hz
i = 0
while not rospy.is_shutdown() and i < 2:
   rate.sleep()
   print("vehicle_3_controller started", i )
   i = i + 1
   rate = rospy.Rate(10) #Hz

# Wait for policy node
print("Vehicle 3.->Waiting for start signal", flush = True)
rospy.wait_for_message('/vehicle_started', Empty, timeout=None)
print("Vehicle 3.->Start signal received", flush = True)

state = SM_INIT
steering = 0.0
while driver.step() != -1 and not rospy.is_shutdown():
   driver.setCruisingSpeed(speed_v3) # SPEED CONTROL km/h - INITIAL SPEED
   driver.setSteeringAngle(steering) # STEERING ANGLE - INITIAL ANGLE
   
   radar_returns = frontal_radar_Webots.getTargets() # from Webots
      
   radar_returns = [r for r in radar_returns if r.distance != 1.0]
   
   #print("STATE=", state, flush = True) 
   #print("V3 pos=", [current_x, current_y, current_a], flush = True)    
   for radar_target in radar_returns:
      if state == SM_INIT:
        # input
        if (-fov <= radar_target.azimuth <= fov and 
             radar_target.distance <= valid_dist
           ):
           v3_free_N = False 
           # output
           print("START V3 swerving", flush = True)
           # transition
           state = SM_TURN_RIGHT_1
      elif state == SM_TURN_RIGHT_1:
        # input
        # output      
        # transition
        if speed_v3 <= 10:
           speed_v3 = max_speed
        steering = calculate_turning_steering(-1.2, 2.9, speed_v3)
        if current_y < 2.5:
           state = SM_TURN_RIGHT_2         
      elif state == SM_TURN_RIGHT_2:
        # input
        # output
        # transition
        if speed_v3 <= 10:
            speed_v3 = max_speed
        steering = calculate_turning_steering(1.2, 2.9, speed_v3)
        
        if current_y > 2.5 or abs(current_a) < 0.05: 
             print("V3 swerving FINISHED", flush = True)
             state = SM_CRUISE        
      elif state == SM_CRUISE:
        # input
        # output
        # transition  
        steering = 0.0             
        state == SM_CRUISE
            
   pub_radar_scan.publish(v3_free_N) # PUBLISHING RADAR MESSAGE

   rate.sleep()
