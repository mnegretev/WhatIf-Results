#!/usr/bin/env python3

# https://cyberbotics.com/doc/reference/supervisor
# https://www.cyberbotics.com/doc/reference/motor
# https://www.cyberbotics.com/doc/reference/solid
# https://cyberbotics.com/doc/reference/worldinfo
# https://www.cyberbotics.com/doc/guide/programming?version=R2021a

import numpy as np
import rospy
import math
from std_msgs.msg import Empty, Float64, Bool
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist
from controller import Supervisor

TIME_STEP = 10
special_robot = Supervisor()

# Cruise speed cars in left lane
def callback_speed_cars_left_lane(msg):
    global speed_cars_left_lane
    # We assume negative speed move vehicles in the opposite direction to the self-driving vehicle
    speed_cars_left_lane = -msg.data

# Cruise speed cars in right lane
def callback_speed_cars_right_lane(msg):
    global speed_cars_right_lane
    speed_cars_right_lane = msg.data

def main():

    global start, speed_cars_left_lane, speed_cars_right_lane, vehicle_3_free_N
    print('STARTING SUPERVISOR FOR WHAT-IF TESTS... November 2024')

    speed_cars_left_lane = 0.0
    speed_cars_right_lane = 0.0

    # https://cyberbotics.com/doc/guide/supervisor-programming
    #cars = [special_robot.getFromDef('vehicle_1'), special_robot.getFromDef('vehicle_2'), special_robot.getFromDef('vehicle_3'), special_robot.getFromDef('vehicle_4'),  special_robot.getFromDef('vehicle_5'), special_robot.getFromDef('vehicle_6'), special_robot.getFromDef('vehicle_7'), special_robot.getFromDef('vehicle_8'), special_robot.getFromDef('vehicle_9'), special_robot.getFromDef('vehicle_10')]
    cars = [special_robot.getFromDef('vehicle_1'),
            special_robot.getFromDef('vehicle_2'),
            special_robot.getFromDef('vehicle_4')
           ]    
    
    tf = []
    for i, car in enumerate(cars):
        if car is not None:
            tf.append(car.getField("translation"))
            values = tf[i].getSFVec3f()
            #print(i, ")", "Initial:", values)
            rand_val = np.random.uniform(-2, 2, 1)
            #print("Random number", rand_val)
            values[1] = values[1] + rand_val
            #print("New y value", values[y])
            tf[i].setSFVec3f(values)
            car.resetPhysics()
     
    bmw = special_robot.getFromDef('BMW_X5')
    v3 = special_robot.getFromDef('vehicle_3')    

    start = False
    rospy.init_node("supervisor_node")
    loop = rospy.Rate(1000/TIME_STEP)

    rospy.Subscriber("/speed_cars_left_lane", Float64,
                     callback_speed_cars_left_lane)
    rospy.Subscriber("/speed_cars_right_lane", Float64,
                     callback_speed_cars_right_lane)

    pub_bmw_pose = rospy.Publisher("/self_driving_pose", Pose2D, queue_size=1)
    pub_car_1_pose  = rospy.Publisher("/car_1_pose", Pose2D, queue_size=1)
    pub_car_2_pose  = rospy.Publisher("/car_2_pose", Pose2D, queue_size=1)
    pub_car_3_pose = rospy.Publisher("/car_3_pose", Pose2D, queue_size=1)
    pub_car_4_pose  = rospy.Publisher("/car_4_pose", Pose2D, queue_size=1)
    '''
    pub_car_5_pose  = rospy.Publisher("/car_5_pose", Pose2D, queue_size=1)
    pub_car_6_pose  = rospy.Publisher("/car_6_pose", Pose2D, queue_size=1)
    pub_car_7_pose  = rospy.Publisher("/car_7_pose", Pose2D, queue_size=1)
    pub_car_8_pose  = rospy.Publisher("/car_8_pose", Pose2D, queue_size=1)
    pub_car_9_pose  = rospy.Publisher("/car_9_pose", Pose2D, queue_size=1)
    pub_car_10_pose  = rospy.Publisher("/car_10_pose", Pose2D, queue_size=1)
    '''

    msg_bmw_pose = Pose2D()
    msg_v3_pose = Pose2D()    
    msg_car_pose = Pose2D()
    
    # initial random position bmw
    rand_val = np.random.uniform(-2, 2, 1)
    translation_field = bmw.getField("translation")
    values = translation_field.getSFVec3f() 
    print("BMW Initial position:", values, flush = True)
    print("BMW Random number", rand_val, flush = True)
    values[0] = values[0] + rand_val
    translation_field.setSFVec3f(values)
    print("BMW New x value", values[0], flush = True)    
    bmw.resetPhysics()    
    
    # initial random position vehicle_3
    # The world could have no v3 vehicle HHAA-25/12/24
    if v3 is not None: 
       rand_val = np.random.uniform(-2, 2, 1)
       translation_field = v3.getField("translation")
       values = translation_field.getSFVec3f() 
       print("V3 Initial position:", values, flush = True)
       print("V3 Random number", rand_val, flush = True)    
       values[1] = values[1] + rand_val
       translation_field.setSFVec3f(values)
       print("V3 New y value", values[1], flush = True)        
       v3.resetPhysics()        
    
    print("Supervisor.->Waiting for start signal")
    rospy.wait_for_message("/policy_started", Empty, timeout=50000.0)
    print("Supervisor.->Start signal received")

    while special_robot.step(TIME_STEP) != -1 and not rospy.is_shutdown():

        for i, car in enumerate(cars):
            if car is not None:     
                values = tf[i].getSFVec3f()
                msg_car_pose.x = values[0]
                msg_car_pose.y = values[1]
                msg_car_pose.theta = values[2]
                
                if msg_car_pose.x < 65.25:
                    car.setVelocity([0, speed_cars_right_lane, 0, 0, 0, 0])
                else:
                    car.setVelocity([0, speed_cars_left_lane, 0, 0, 0, 0])

                if i == 0:
                    pub_car_1_pose.publish(msg_car_pose)  
                elif i == 1:
                    pub_car_2_pose.publish(msg_car_pose)               
                elif i == 2:
                    pub_car_4_pose.publish(msg_car_pose)               
                '''
                elif i == 4:
                    pub_car_5_pose.publish(msg_car_pose)
                elif i == 5:
                    pub_car_6_pose.publish(msg_car_pose)               
                elif i == 6:
                    pub_car_7_pose.publish(msg_car_pose)
                elif i == 7:
                    pub_car_8_pose.publish(msg_car_pose)               
                elif i == 8:
                    pub_car_9_pose.publish(msg_car_pose)
                elif i == 9: 
                    pub_car_10_pose.publish(msg_car_pose)
                '''    

        bmw_pose = bmw.getPosition()
        bmw_orient = bmw.getOrientation()
        msg_bmw_pose.x = bmw_pose[0]
        msg_bmw_pose.y = bmw_pose[1]
        msg_bmw_pose.theta = math.atan2(bmw_orient[3], bmw_orient[0])
        pub_bmw_pose.publish(msg_bmw_pose)
        
        if v3 is not None:
           v3_pose = v3.getPosition()
           v3_orient = v3.getOrientation()
           msg_v3_pose.x = v3_pose[0]
           msg_v3_pose.y = v3_pose[1]
           msg_v3_pose.theta = math.atan2(v3_orient[3], v3_orient[0])
           pub_car_3_pose.publish(msg_v3_pose)
        
        #print("bmw_x:", msg_bmw_pose.x, "bmw_y:", msg_bmw_pose.y, "bmw_theta:", msg_bmw_pose.theta, flush = True)
        #print("v3_x:", msg_v3_pose.x, "v3_y:", msg_v3_pose.y, "v3_theta:", msg_v3_pose.theta, flush = True)        
        

        loop.sleep()


if __name__ == "__main__":
    try:
        main()
    except:
        pass
