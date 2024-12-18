#!/usr/bin/env python3
"""
This node detects potential front (or sideswipe) collisions using radar readings and knowledge about the current state-action pair.
"""

# https://sensible4.fi/technology/articles/obstacle-detection-and-tracking-system-odts-enables-a-smooth-safe-ride-for-everyone/
# https://cyberbotics.com/doc/reference/radar?tab-language=python
# https://cyberbotics.com/doc/guide/radar-sensors?version=R2022a
# https://cyberbotics.com/doc/reference/radar
# http://docs.ros.org/en/noetic/api/radar_msgs/html/index-msg.html
# http://docs.ros.org/en/noetic/api/radar_msgs/html/msg/RadarReturn.html
# https://index.ros.org/p/radar_msgs/github-ros-perception-radar_msgs/
# http://docs.ros.org/en/noetic/api/webots_ros/html/index-msg.html
# http://docs.ros.org/en/noetic/api/webots_ros/html/msg/RadarTarget.html
# http://wiki.ros.org/ainstein_radar/Tutorials/Target%20tracking%20from%20raw%20radar%20detections

# IMPORTANT: sudo apt-get install ros-noetic-radar-msgs

import math
import rospy
import numpy
from std_msgs.msg import Bool, Float64MultiArray, Float64, String, Empty 
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Pose2D
from radar_msgs.msg import RadarReturn, RadarScan
import ros_numpy

    
def callback_free_N(msg):
    global free_N
    free_N = msg.data

def callback_free_NW(msg):
    global free_NW
    free_NW = msg.data

def callback_free_W(msg):
    global free_W
    free_W = msg.data
    
def callback_free_NE(msg):
    global free_NE
    free_NE = msg.data    

def callback_free_E(msg):
    global free_E
    free_E = msg.data    

def callback_curr_lane(msg):
    global curr_lane
    curr_lane = msg.data   
    
def callback_action(msg):
    global action
    action = msg.data             
    
def callback_sdc_vel(msg):
    global sdc_vel_kh
    sdc_vel_kh = msg.data 
        
def callback_radar(msg):
    global radar_scan
    radar_scan = msg 
    
def callback_point_cloud(msg):
    global xyz
    xyz = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(msg)

def main():
    global latent_collision, curr_time, sdc_vel_kh, curr_lane, free_N, free_NW, free_W, free_NE, free_E, action, radar_scan, free_left, free_right    
    
    print("INITIALIZING LATENT_COLLISION_DETECTOR...", flush=True)
    rospy.init_node("latent_collision_detector")
    rate = rospy.Rate(10)
        
    sdc_curr_pos = Pose2D()   
    car_1_pos = Pose2D() 
    car_2_pos = Pose2D()    

    radar_scan = RadarScan()    
    radar = RadarReturn()
    closest_obst_front = RadarReturn()
                
    rospy.Subscriber("/current_lane", Bool, callback_curr_lane)    
    rospy.Subscriber("/speed", Float64, callback_sdc_vel)
    
    rospy.Subscriber("/free/north", Bool, callback_free_N)              
    rospy.Subscriber("/free/north_west", Bool, callback_free_NW)
    rospy.Subscriber("/free/west", Bool, callback_free_W)
    rospy.Subscriber("/free/north_east", Bool, callback_free_NE)
    rospy.Subscriber("/free/east", Bool, callback_free_E) 
    rospy.Subscriber("/action", String, callback_action)   
    rospy.Subscriber("/frontal_radar_scan", RadarScan, callback_radar)
    rospy.Subscriber('/point_cloud', PointCloud2, callback_point_cloud)
    
    pub_latent_collision  = rospy.Publisher("/latent_collision", Bool, queue_size=1)    
    
    latent_collision = False
    
    # Extras
    sdc_vel_kh = 0.0
        
    free_N = True
    free_NW = True
    free_W  = True
    free_NE = True
    free_E  = True
    curr_lane = True
    action = "NA"   

    right_side = False
    left_side = False    
    free_right = False
    free_left = False
    xyz = numpy.empty((0, 3))  

    # Parameters for the radar
    min_dist_radar_ref = 1    # Minimum distance (in meters)
    max_dist_radar_ref = 45   # Maximum distance (in meters)
    lateral_vision = 3              # The radar sees 3m on each side

    # Field of view (FoV) at minimum and maximum distances
    radar_ref = {
         "min_dist": 1, # Minimum distance (in meters)
         "max_dist": 10, # Maximum distance (in meters)
         # The radar should sees 3m on each side
         "max_fov": math.atan2(3, min_dist_radar_ref),
         # Max FoV at 1m
         "min_fov": math.atan2(3, max_dist_radar_ref)  
         # Min FoV at 45m
    }
    radar_ref["dist"] = radar_ref["max_dist"]
    radar_ref["fov"] = radar_ref["min_fov"]    
    valid_dist = 25 # distance to a vehicle in front that poses a potential crash

    # Wait for policy node
    rospy.wait_for_message('/policy_started', Empty, timeout=None)
    
    # Dictionary of state
    state = {}
    
    # infinite loop
    while not rospy.is_shutdown():

       latent_collision = False
       obst_at_front = False 
       obst_opposite_dir = False 
       obst_stationary = False 
       obst_same_dir = False
       obst_vel = 0.0
       obst_dist = 1000000 # meters
    
       # Patch   
       if curr_lane:
         free_NE = free_N
       else:
         free_NW = free_N    
    
       state.clear()
       #state["action"] = action
       state["free_NW"] = free_NW
       state["free_W"] = free_W
       state["free_NE"] = free_NE
       state["free_E"] = free_E
       state["curr_lane"] = curr_lane
       
       xyz = xyz[(xyz[:,2] > -1) & (xyz[:,2] < 0.3) ] #Filters points on floor and higher points
       left_side  = xyz[ (xyz[:,0] > -6) & (xyz[:,0] <  6) & 
                         (xyz[:,1] < 8) & (xyz[:,1] >  1.5)
                       ]

       right_side  = xyz[ (xyz[:,0] > -6) & (xyz[:,0] <  6) & 
                          (xyz[:,1] > -8) & (xyz[:,1] <  -1.5)
                        ]     
                        
       free_right  = right_side.shape[0] < 10                    
       free_left   = left_side.shape[0] < 10        
         
       # remove unnecessary data first 
       closest_obst_front.range = -1
       radar_scan.returns = [r for r in radar_scan.returns if r.range != 1.0]
       # If the car is swerving enlarge FoV 
       if action == "swerve_left" or action == "swerve_right":
          radar_ref["fov"] = 0.8725
        
       for radar in radar_scan.returns:
         if (-radar_ref["fov"] <= radar.azimuth 
                    <= radar_ref["fov"] and radar.range <= valid_dist
            ):
            if radar.range < obst_dist:
              obst_dist = radar.range
              closest_obst_front = radar 
       
       #print("FoV=", radar_ref["fov"], flush=True) 
       #print("closest_obst_front", closest_obst_front,flush=True)
              
       radar_ref["fov"] = radar_ref["min_fov"]  
       
       # Conditions to warn a potential collision when turning
       if (action == "swerve_left" or action == "change_to_left") and not free_right:
           latent_collision = True
           print("Obstacle approaching from the right while swerving left", flush = True)
       elif (action == "swerve_right"  or action == "change_to_right") and not free_left:
           latent_collision = True
           print("Obstacle approaching from the left while swerving right", flush = True)
       elif action == 'change_to_right' and curr_lane:
          latent_collision = True
          print("Latent collision while changing to right on right lane", flush = True)
       elif action == 'change_to_left' and not curr_lane:
          latent_collision = True
          print("Latent collision while changing to left on left lane", flush = True)
       elif action == 'change_to_left' and curr_lane and (not free_NW or not free_W):
          latent_collision = True
          print("Latent collision while changing to left with obstacles", flush = True)         
       elif action == 'change_to_right' and (not curr_lane and (not free_NE or not free_E)):   
          latent_collision = True
          print("Latent collision while changing to right with obstacles", flush = True)              
       # Get the closest vehicle in front    
       elif closest_obst_front.range != -1:

          latent_collision = True 
          print("Obstacle in front", flush = True)

          # Interpolation of FoV based on the distance of the obstacle
          fov_range = radar_ref["max_fov"] - radar_ref["min_fov"]
          dist_ratio = ((radar_ref["max_dist"] -
                         closest_obst_front.range) /
                        (radar_ref["max_dist"] - radar_ref["min_dist"])
                       ) 
          radar_ref["fov"] = radar_ref["min_fov"] + (fov_range * dist_ratio) 
          
          # self-driving car (sdc_vel_kh) from km/h to m/s         
          sdc_vel_ms = (sdc_vel_kh * (1000)) / 3600       
          # V_AB = V_A - V_B ==> V_B = V_A + V_AB
          obst_vel = (sdc_vel_ms +
                            closest_obst_front.doppler_velocity
                           ) 
          if -1.0 < obst_vel <= 1.0:
             obst_vel = 0.0 # Assume the obstacle is stationary
             obst_stationary = True
          elif obst_vel < -1.0:
             obst_opposite_dir = True   
          else:                   
             obst_same_dir = True

          #print("Obst vars", [obst_vel, obst_stationary, obst_opposite_dir, obst_same_dir], flush = True)                 
        
          safe_dist = 15              
          # Conditions of potential collisions 
          if obst_stationary or obst_opposite_dir:
             print("Obstacle stationary or in opposite direction", flush = True)
          elif action == "cruise" and (obst_dist < safe_dist and obst_vel < sdc_vel_ms):
             print("Obstacle travelling in direction possibly at a slower velocity", flush = True)


                
       '''           
       else:
          print("No crash condition detected", flush = True)   
       '''        
       pub_latent_collision.publish(latent_collision)               

       #if latent_collision:
       #   print("Warning! Potential collision detected", flush = True)  
          
       rate.sleep()
    

if __name__ == "__main__":
    main()    


