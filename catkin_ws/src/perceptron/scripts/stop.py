#!/usr/bin/env python3
"""
This node stop the car by killing the nodes that control the car and sets the car speed to 0
  
"""
import os
import rospy
from std_msgs.msg import Float64, Empty, Bool, String
from rosgraph_msgs.msg import Clock 

def mysleep(secs):
    global curr_time

    init_time = curr_time        
    diff = 0.0
    while diff <= secs or not rospy.is_shutdown(): # and not rospy.is_shutdown():
       diff  = curr_time - init_time
       
def callback_sim_time(msg):
    global curr_time            
    sim_time = msg
    sim_secs = sim_time.clock.secs 
    sim_nsecs = sim_time.clock.nsecs
    curr_time = sim_secs + sim_nsecs / (10**9)        
   
def callback_success(msg):
    global success
    success = msg.data    

def publish_stop():
    global pub_action
    pub_action.publish("stop") 
    
def stop_velocity():
    global pub_speed
    speed = 0.0  
    pub_speed.publish(speed) 
    
def callback_goal_reached(msg):
    global goal_reached
    goal_reached = msg.data             

def main():

    global success, pub_speed, pub_action, goal_reached
            
    print('INITIALIZING STOP NODE...', flush=True)
    rospy.init_node('stop')
    rate = rospy.Rate(10)

    success = True
    goal_reached = False

    rospy.Subscriber("/success", Bool, callback_success) 
    #rospy.Subscriber("/clock", Clock, callback_sim_time)        
    rospy.Subscriber("/goal_reached", Bool, callback_goal_reached)      
    pub_speed = rospy.Publisher('/speed', Float64, queue_size=1)
    pub_action = rospy.Publisher('/action', String, queue_size=1)    

    while not rospy.is_shutdown():
        if success == False or goal_reached:

            print("STOP: Starting system shutdown...",  flush = True)  
            rate = rospy.Rate(200)
            rate.sleep()
            
            os.system("rosnode kill /policy")
            publish_stop()            
            stop_velocity()
            os.system("rosnode kill /logger")            

            os.system("rosnode kill /behaviors")
            os.system("rosnode kill /lane_detector")
            os.system("rosnode kill /lane_identification")
            os.system("rosnode kill /lane_tracking_control_P")          
            os.system("rosnode kill /obstacle_detector")
            os.system("rosnode kill /crash_detector")
            os.system("rosnode kill /latent_collision_detector")            

            print("STOP: System shutdown finished.", end="", flush = True) 

            os.system("rosnode kill /stop")     
                   
        else: # do_nothing
            continue

        rate.sleep()
    

if __name__ == "__main__":
    main()

    

