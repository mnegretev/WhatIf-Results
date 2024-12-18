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

# States
DFA_INIT = 0
DFA_PERCEPTRON = 10
DFA_WHATIF = 20

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

def callback_latent_collision(msg):
    global latent_collision
    latent_collision = msg.data

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

def get_WhatIf_action(obs_state, action, df_whatif, df_choices):
    # Apply the filter using the criteria
    filtered_rows = df_whatif[
      (df_whatif['action'] == action) &
      (df_whatif['curr_lane'] == obs_state['curr_lane']) &
      (df_whatif['free_E'] == obs_state['free_E']) &
      (df_whatif['free_NE'] == obs_state['free_NE']) &
      (df_whatif['free_NW'] == obs_state['free_NW']) &
      (df_whatif['free_SE'] == obs_state['free_SE']) &
      (df_whatif['free_SW'] == obs_state['free_SW']) &
      (df_whatif['free_W'] == obs_state['free_W'])
    ]
            
    # Check if there are any matches
    if not filtered_rows.empty: 
       # Select one row and display the 'iaction' value
       alternatives = pd.DataFrame(columns=['swerve_left',
                                    'swerve_right', 
                                    'cruise', 
                                    'keep', 
                                    'change_to_left', 
                                    'change_to_right']
                                  )
       iactions = filtered_rows['iaction'].tolist()
       alternatives.loc[0] = [0] * len(alternatives.columns)
       for iaction in iactions:
          if iaction in alternatives.columns:
             alternatives.at[0, iaction] = 1

       matching_row = df_choices[ (
df_choices['swerve_left'] == alternatives.loc[0, 'swerve_left']) & (df_choices['swerve_right'] == alternatives.loc[0, 'swerve_right']) & (df_choices['cruise'] == alternatives.loc[0, 'cruise']) & (df_choices['keep'] == alternatives.loc[0, 'keep']) & (df_choices['change_to_left'] == alternatives.loc[0, 'change_to_left']) & (df_choices['change_to_right'] == alternatives.loc[0, 'change_to_right'])]

       if not matching_row.empty:
          if curr_lane:  
             action = matching_row['right_lane'].values[0]
          else:
             action = matching_row['left_lane'].values[0]
          abort = True                
       else:
          print("ERROR: no matching rows found in choices. Default action:", end=" ", flush = True)
          action = "NA"
               
    else:
       print("ERROR: no matching rows found in counterfactuals. Default action:", end=" ", flush = True)
       action = "NA"
    
    return action   
    
def publish_action(action, prev_action, abort, obs_state, prev_obs_state, model, latent_collision, prev_latent_collision):
    # Finishing the output in every transition

    if model == "MLP":
       action_str = "MLP action=" + action
    else:
       action_str = "WhatIf action=" + action
    
    if (not all(obs_state[key] == prev_obs_state[key] for key in obs_state)) or prev_latent_collision != latent_collision or prev_action != action:
       print("latent_collision", latent_collision,  
              obs_state, 
              "abort=", abort,
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
          if not abort:             
             print("Waiting for the action", action, "to finish... ", 
                    flush = True, sep=" ", end=""
                  )
             rospy.wait_for_message("/action_finished", Bool, timeout=10000.0) 
             print("Done.", sep=" ", flush = True)       
                  

            
def main(speed_left, speed_right, MLP_path, counterfactuals_path, counterfactual_choices_path):
    global free_N, free_NW, free_W, free_SW, free_NE, free_E, free_SE,  curr_lane, action_finished, latent_collision
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
    rospy.Subscriber("/latent_collision", Bool, callback_latent_collision)
       
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
       
    # Load Counterfactuals
    try:       
       df_whatif = pd.read_csv(counterfactuals_path)
    except Exception as error:
       print("Error loading counterfactuals:", error)  
       sys.exit("Please enter to the directory ../decision_models and make shure the file is in the directory")
       
    # Load Counterfactual choices
    try:  
       df_choices = pd.read_csv(counterfactual_choices_path) 
    except Exception as error:
       print("Error loading counterfactual choices:", error)  
       sys.exit("Please enter to the directory ../decision_models and make shure the file is in the directory")       
    
    action = "cruise" # The procedure should start with a valid action 
    prev_action = "NA"                   

    latent_collision = False
    prev_latent_collision = None
    abort = None

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

    first_time = True

    # Pause policy.py a little bit
    rate = rospy.Rate(1) # Hz
    i = 0
    while not rospy.is_shutdown() and i < 2:
      pub_policy_started.publish()
      rate.sleep()
      print("Publishing policy_started", i )
      i = i + 1
    rate = rospy.Rate(10) #Hz
    
    state = DFA_INIT
    while not rospy.is_shutdown():
      pub_policy_started.publish()
      pub_speed_cars_left_lane.publish(vel_cars_left_lane)
      pub_speed_cars_right_lane.publish(vel_cars_right_lane) 
      
      #print("STATE=", state, flush = True)
        
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

      #print("state=",state, "prev_latent_collision=", prev_latent_collision, "latent_collision=", latent_collision, flush=True)
      #print("obs_state=", obs_state, flush=True)
      if (not all(obs_state[key] == prev_obs_state[key] for key in obs_state)) or not (prev_latent_collision and latent_collision):
         if state == DFA_INIT:
            # input
            if latent_collision:
               # output
               abort = False
               pub_abort.publish(abort)               
               action = get_WhatIf_action(obs_state, 
                                 action, 
                                 df_whatif, 
                                 df_choices
                                )
                                
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "WHATIF", latent_collision, prev_latent_collision)      
               # Transition
               state = DFA_PERCEPTRON
            else:
               # output
               abort = True
               pub_abort.publish(abort)
               action = get_MLP_action(obs_state, mlp_model)
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "MLP", latent_collision, prev_latent_collision)
               # Transition
               state = DFA_WHATIF            
         elif state == DFA_PERCEPTRON:
            # input
            if latent_collision:
               # output
               abort = False
               pub_abort.publish(abort)
               action = get_WhatIf_action(obs_state, 
                                 action, 
                                 df_whatif, 
                                 df_choices
                                )
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "WHATIF", latent_collision, prev_latent_collision)
               # Transition
               state = DFA_WHATIF
            else:
               # output
               abort = True
               pub_abort.publish(abort)
               action = get_MLP_action(obs_state, mlp_model)
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "MLP", latent_collision, prev_latent_collision)
               # Transition
               state = DFA_PERCEPTRON
         elif state == DFA_WHATIF:
            # input
            if latent_collision:
               # output
               abort = False
               pub_abort.publish(abort)
               action = get_WhatIf_action(obs_state, 
                                 action, 
                                 df_whatif, 
                                 df_choices
                                )
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "WHATIF", latent_collision, prev_latent_collision)
               # Transition
               state = DFA_WHATIF
            else:
               # output
               abort = True
               pub_abort.publish(abort)
               action = get_MLP_action(obs_state, mlp_model)
               publish_action(action, prev_action, abort, obs_state, prev_obs_state, "MLP", latent_collision, prev_latent_collision)
               # Transition
               state = DFA_PERCEPTRON

         # Keep current observed state-action pair   
         prev_obs_state = obs_state.copy()
         # Store previous state of latent collision
         prev_latent_collision = latent_collision
         prev_action = action
                               
      rate.sleep()
        
        
        
###############################
###
###        
if __name__ == "__main__":

    speed_left = 0
    speed_right = 0
    MLP = ""
    counterfactuals = ""
    counterfactual_choices = ""    

    if len(sys.argv) != 6:
        print("Usage: rosrun opposite_direction MLP_control.py speed_left=value1 (in m/s) speed_right=value2 (in m/s) MLP=filename.mlp  counterfactuals=counterfactuals.csv  choices=counterfactuals_action_choice.csv\n"
              "Suggested values: speed_left=5 speed_right=3 MLP=MLP_10.mlp counterfactuals=counterfactuals.csv choices=counterfactuals_action_choice.csv")
    else:
        try:
            # Parse arguments
            args = [arg.split('=') for arg in sys.argv[1:6]]
                        
            if not all(len(arg) == 2 for arg in args):
                raise ValueError("Arguments must be in the format speed_left=value (in m/s) and speed_right=value (in m/s) and MLP=filename.mlp and  counterfactuals=counterfactuals.csv counterfactual_choices=counterfactuals_action_choice.csv")

            # Extract and convert values
            expected_keys = ["speed_left", "speed_right", "MLP", "counterfactuals", "choices"]
            if all(arg[0] == expected for arg, expected in zip(args, expected_keys)):
               speed_left, speed_right = map(float, (args[0][1], args[1][1]))
               MLP, counterfactuals, counterfactual_choices = (arg[1] for arg in args[2:])
               MLP_path = os.path.join(rospkg.RosPack().get_path('opposite_direction'), 'decision_models', MLP)
               #print(MLP_path, flush=True)
               counterfactuals_path =  os.path.join(rospkg.RosPack().get_path('opposite_direction'),
                  'decision_models', counterfactuals)
               #print(counterfactuals_path, flush=True)
               counterfactual_choices_path =  os.path.join(rospkg.RosPack().get_path('opposite_direction'), 'decision_models', counterfactual_choices)
                                
            else:
                raise ValueError("Arguments must be named speed_left,  speed_right, MLP, counterfactuals and choices")
            
            print(f"Running with speed_left={speed_left} and speed_right={speed_right} MLP={MLP} counterfactuals={counterfactuals} choices={counterfactual_choices}")
            main(speed_left=speed_left, speed_right=speed_right, MLP_path=MLP_path, counterfactuals_path=counterfactuals_path, counterfactual_choices_path=counterfactual_choices_path)
        except ValueError as e:
            print(f"Error: {e}")
        except rospy.ROSInterruptException:
            pass    

