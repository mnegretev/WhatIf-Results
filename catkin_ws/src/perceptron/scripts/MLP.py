#!/usr/bin/env python3
"""
This node implements the action policy of the self-driving car
obtained from modeling and training a multilayer perceptron using Sklearn.
This node provides several functions to detect 
other vehicles around the car and as a consequence to execute one of 6 actions available. If there is are potential collisions, counterfactual queries will be performed. 
"""
import rospy
from std_msgs.msg import Float64MultiArray, Empty, Bool, String, Float64
from rosgraph_msgs.msg import Clock 
import sys
import pandas as pd
import pickle
import time
import numpy as np
import os
import rospkg

def callback_free_N(msg):
    global free_N
    free_N = msg.data

def callback_free_NW(msg):
    global free_NW
    free_NW = msg.data

def callback_free_W(msg):
    global free_W
    free_W = msg.data
    
def callback_free_SW(msg):
    global free_SW
    free_SW = msg.data
    
def callback_free_NE(msg):
    global free_NE
    free_NE = msg.data    

def callback_free_E(msg):
    global free_E
    free_E = msg.data    

def callback_free_SE(msg):
    global free_SE
    free_SE = msg.data    
        
def callback_curr_lane(msg):
    global curr_lane
    curr_lane = msg.data
    
def callback_change_lane_finished(msg):
    global action_finished
    action_finished = msg.data    

def cruise():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action    
    pub_keep_distance.publish(False)
    pub_change_lane_on_left.publish(False)
    pub_change_lane_on_right.publish(False)
    pub_swerve_right.publish(False)    
    pub_swerve_left.publish(False)                
    pub_cruise.publish(True)    

def keep_distance():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action, curr_lane
    pub_cruise.publish(False)
    pub_change_lane_on_left.publish(False)
    pub_change_lane_on_right.publish(False)
    pub_swerve_right.publish(False)    
    pub_swerve_left.publish(False)         
    pub_keep_distance.publish(True)    

def change_lane_on_left():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_swerve_right, pub_swerve_left, pub_action, curr_lane

    pub_keep_distance.publish(False)
    pub_cruise.publish(False)    
    pub_change_lane_on_right.publish(False)
    pub_swerve_right.publish(False)    
    pub_swerve_left.publish(False)     
    pub_change_lane_on_left.publish(True)
    
def change_lane_on_right():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action, curr_lane

    pub_keep_distance.publish(False)
    pub_cruise.publish(False)    
    pub_change_lane_on_left.publish(False)
    pub_swerve_right.publish(False)    
    pub_swerve_left.publish(False)         
    pub_change_lane_on_right.publish(True)  
    
def swerve_right():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action    
    pub_keep_distance.publish(False)
    pub_change_lane_on_left.publish(False)
    pub_change_lane_on_right.publish(False)    
    pub_cruise.publish(False)    
    pub_swerve_left.publish(False)    
    pub_swerve_right.publish(True)    
    
def swerve_left():
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action    
    pub_keep_distance.publish(False)
    pub_change_lane_on_left.publish(False)
    pub_change_lane_on_right.publish(False)    
    pub_cruise.publish(False)    
    pub_swerve_right.publish(False)    
    pub_swerve_left.publish(True)   
    
    
def get_MLP_action(obs_state, model):
    try:
       X = pd.DataFrame(columns=["curr_lane", 
                                 "free_E", 
                                 "free_NE", 
                                 "free_NW", 
                                 "free_SE", 
                                 "free_SW", 
                                 "free_W"
                                ]
                       )
       X.loc[len(X)] = obs_state

    except Exception as error:
      print("An error occurred constructing predictors:", error) 
      action = "NA"
                
    try:
      y = model.predict(X)
      action = y[0]
    except Exception as error:
      print("An error occurred getting prediction:", error)
      action = "NA"

    return action
    
def publish_action(action, prev_action, obs_state, prev_obs_state, model):
    # Finishing the output in every transition

    if model == "MLP":
       action_str = "MLP action=" + action
    
    if (not all(obs_state[key] == prev_obs_state[key] for key in obs_state)) or prev_action != action:
       print(obs_state,
              action_str,  
              sep = " ", flush = True
            )    
              
       pub_action.publish(action)

       if action == "cruise":  
          cruise()                  
       elif action == "keep":
          keep_distance()        
       elif action == "change_to_left":
          change_lane_on_left()
       elif action == "change_to_right":
          change_lane_on_right()
       elif action == "swerve_left":
          swerve_left()
       elif action == "swerve_right":
          swerve_right()
               
       else:
          print("Unknown action=", action, flush = True)   
       
       if action != "cruise" and action != "keep":
          print("Waiting for the action", action, "to finish... ", 
                 flush = True, sep=" ", end=""
               )
          rospy.wait_for_message("/action_finished", Bool, timeout=10000.0) 
          print("Done.", sep=" ", flush = True)       
                  

            
def main(speed_left, speed_right, MLP_path):
    global free_N, free_NW, free_W, free_SW, free_NE, free_E, free_SE,  curr_lane, action_finished
    global pub_keep_distance, pub_cruise, pub_change_lane_on_left, pub_change_lane_on_right, pub_swerve_right, pub_swerve_left, pub_action, pub_action
    
    vel_cars_left_lane = int(speed_left)
    vel_cars_right_lane = int(speed_right)    
    
    print("INITIALIZING POLICY...", flush=True)
    rospy.init_node("policy")
    rate = rospy.Rate(10) #Hz
       
    rospy.Subscriber("/free/north", Bool, callback_free_N)              
    rospy.Subscriber("/free/north_west", Bool, callback_free_NW)
    rospy.Subscriber("/free/west", Bool, callback_free_W)
    rospy.Subscriber("/free/south_west", Bool, callback_free_SW)
    rospy.Subscriber("/free/north_east", Bool, callback_free_NE)        
    rospy.Subscriber("/free/east", Bool, callback_free_E)    
    rospy.Subscriber("/free/south_east", Bool, callback_free_SE)
    rospy.Subscriber("/current_lane", Bool, callback_curr_lane)
       
    pub_policy_started  = rospy.Publisher("/policy_started", Empty, queue_size=1)
    pub_cruise = rospy.Publisher("/cruise/enable", Bool, queue_size=1)
    pub_keep_distance  = rospy.Publisher("/follow/enable", Bool, queue_size=1)
    pub_change_lane_on_left = rospy.Publisher("/start_change_lane_on_left", Bool, queue_size=1)
    pub_change_lane_on_right = rospy.Publisher("/start_change_lane_on_right", Bool, queue_size=1)    
    pub_action = rospy.Publisher("/action", String, queue_size=1)
    pub_abort = rospy.Publisher("/abort", Bool, queue_size=1)    
    
    pub_speed_cars_left_lane = rospy.Publisher("/speed_cars_left_lane", Float64, queue_size=1)
    pub_speed_cars_right_lane = rospy.Publisher("/speed_cars_right_lane", Float64, queue_size=1)     

    pub_swerve_right = rospy.Publisher("/start_swerve_right", Bool, queue_size=1)      
    pub_swerve_left = rospy.Publisher("/start_swerve_left", Bool, queue_size=1)
    
    print(MLP_path, flush=True)    
    try:
       mlp_model = pickle.load(open(MLP_path, 'rb'))  
    except Exception as error:
       print("Error loading MLP model:", error)  
       sys.exit("Please enter to the subdirectory ../decision_models and run 'sh script.sh' on terminal before coming back")
    
    action = "cruise" # The procedure should start with a valid action 
    prev_action = "NA"                   

    abort = False

    curr_lane = None
    free_N = None
    free_E  = None
    free_NE = None    
    free_NW = None
    free_SE = None
    free_SW = None
    free_W  = None
              
    # Dictionary of obs_state
    obs_state = {}
    obs_state["curr_lane"] = curr_lane
    obs_state["free_E"] = free_E  
    obs_state["free_NE"] = free_NE      
    obs_state["free_NW"] = free_NW
    obs_state["free_SE"] = free_SE
    obs_state["free_SW"] = free_SW    
    obs_state["free_W"] = free_W
    
    prev_obs_state = obs_state.copy()

    # Pause policy.py a little bit
    rate = rospy.Rate(1) # Hz
    i = 0
    while not rospy.is_shutdown() and i < 2:
      pub_policy_started.publish()
      rate.sleep()
      print("Publishing policy_started", i )
      i = i + 1
    rate = rospy.Rate(10) #Hz
    
    while not rospy.is_shutdown():
      pub_policy_started.publish()
      pub_speed_cars_left_lane.publish(vel_cars_left_lane)
      pub_speed_cars_right_lane.publish(vel_cars_right_lane) 
        
      # Patch  
      if curr_lane:
        free_NE = free_N
      else:
        free_NW = free_N

      # Check if the order is correct to feed the MLP
      # Truth values vs string ¿which data type is used?
      obs_state.clear()
      obs_state["curr_lane"] = curr_lane
      obs_state["free_E"] = free_E  
      obs_state["free_NE"] = free_NE              
      obs_state["free_NW"] = free_NW
      obs_state["free_SE"] = free_SE
      obs_state["free_SW"] = free_SW
      obs_state["free_W"] = free_W

      if (not all(obs_state[key] == prev_obs_state[key] for key in obs_state)):
         # output
         pub_abort.publish(abort)               
         action = get_MLP_action(obs_state, mlp_model)
         publish_action(action, prev_action, obs_state, prev_obs_state, "MLP")

         # Keep current observed state-action pair   
         prev_obs_state = obs_state.copy()
         # Store previous state of latent collision
         prev_action = action
                               
      rate.sleep()
        
        
        
###############################
###
###        
if __name__ == "__main__":

    speed_left = 0
    speed_right = 0
    MLP = ""

    if len(sys.argv) != 4:
        print("Usage: rosrun perceptron MLP_control.py speed_left=value1 (in km/h) speed_right=value2 (in m/s) MLP=filename.mlp\n"
              "Suggested values: speed_left=15 speed_right=3 MLP=MLP_10.mlp")
    else:
        try:
            # Parse arguments
            args = [arg.split('=') for arg in sys.argv[1:4]]  # <-- Change to 1:4 to capture all 3 arguments
                        
            if not all(len(arg) == 2 for arg in args):
                raise ValueError("Arguments must be in the format speed_left=value (in km/h), speed_right=value (in m/s), and MLP=filename.mlp")

            # Extract and convert values
            expected_keys = ["speed_left", "speed_right", "MLP"]
            if all(arg[0] == expected for arg, expected in zip(args, expected_keys)):
                speed_left, speed_right = map(float, (args[0][1], args[1][1]))
                MLP = args[2][1]
                MLP_path = os.path.join(rospkg.RosPack().get_path('perceptron'), 'decision_models', MLP)         
            else:
                raise ValueError("Arguments must be named speed_left, speed_right, and MLP")
            
            print(f"Running with speed_left={speed_left}, speed_right={speed_right}, and MLP={MLP}")
            main(speed_left=speed_left, speed_right=speed_right, MLP_path=MLP_path)
        except ValueError as e:
            print(f"Error: {e}")
        except rospy.ROSInterruptException:
            pass
