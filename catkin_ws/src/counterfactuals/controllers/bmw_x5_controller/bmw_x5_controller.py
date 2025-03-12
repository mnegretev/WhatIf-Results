#!/usr/bin/env python3

# https://cyberbotics.com/doc/reference/supervisor
# https://www.cyberbotics.com/doc/reference/motor
# https://www.cyberbotics.com/doc/reference/solid
# https://cyberbotics.com/doc/reference/worldinfo
# https://www.cyberbotics.com/doc/guide/programming?version=R2021a
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
from vehicle import Driver
from controller import Camera, Lidar, Accelerometer, Radar #Gyro,GPS

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image, PointCloud2, PointField, NavSatFix, NavSatStatus, Imu
from rosgraph_msgs.msg import Clock
from radar_msgs.msg import RadarReturn, RadarScan


# INIT DRIVER
# https://cyberbotics.com/doc/automobile/driver-library
driver = Driver()
driver.setCruisingSpeed(0.0) # SPEED CONTROL km/h - INITIAL SPEED
driver.setSteeringAngle(0.0) # STEERING ANGLE - INITIAL ANGLE

# CONSTANTS
TIME_STEP = int(driver.getBasicTimeStep())

# INIT SENSORS
camera = Camera('camera')  # GET CAMERA FROM DEVICES
camera.enable(TIME_STEP)    

lidar = Lidar('Velodyne HDL-64E')
lidar.enable(TIME_STEP)
lidar.enablePointCloud()

accel = Accelerometer('accelerometer')
accel.enable(TIME_STEP)

# Sms UMRR 0a31: Min radar range= 1.0 Max radar range= 45.0 horiz_radar_fov= 1.745 (45 deg each side) vertical_radar_fov= 0.1745
frontal_radar_Webots = Radar('Sms UMRR 0a31')
frontal_radar_Webots.enable(TIME_STEP)

# INIT GPS
# gps = GPS('gps')
# gps.enable(TIME_STEP)

# # INIT GYRO
# gyro = Gyro('gyro')
# gyro.enable(TIME_STEP)


# Cruise speed callback
def callback_cruise_speed( msg ):
  driver.setCruisingSpeed(msg.data)

# STEERING ANGLE CALLBACK
def callback_steering_angle(msg):
  driver.setSteeringAngle(-msg.data)

# MAIN FUNCTION
def main():

  # INIT ROS
  print('STARTING BMW X5 CONTROLLER NODE (August 2024)...')
  rospy.init_node('bmw_x5_controller')
  rate = rospy.Rate(1000/TIME_STEP)

  print('SIMULATION FOR THE  AUTOMODELCAR LEAGUE OF THE MEXICAN ROBOTICS TOURNAMENT')
  print('TO MOVE THE VEHICLE, USE THE CORRESPONDING TOPICS')
  print('CHECK ONLINE DOCUMENTATION AT https://github.com/mnegretev/TMR-2022-AutoModelCar')
  
  # IMAGE MESSAGE
  msg_image = Image()
  msg_image.height = camera.getHeight()
  msg_image.width = camera.getWidth()
  msg_image.is_bigendian = False
  msg_image.step = camera.getWidth() * 4
  msg_image.encoding = 'bgra8'

  # POINT CLOUD2 MESSAGE 
  msg_point_cloud = PointCloud2()
  msg_point_cloud.header.stamp = rospy.Time.now()
  msg_point_cloud.header.frame_id = 'lidar_link'  
  msg_point_cloud.height = 1
  msg_point_cloud.width = lidar.getNumberOfPoints()
  msg_point_cloud.point_step = 20
  msg_point_cloud.row_step = 20 * lidar.getNumberOfPoints()
  msg_point_cloud.is_dense = False
  msg_point_cloud.fields = [
    PointField(name = 'x', offset = 0, datatype = PointField.FLOAT32, count = 1),
    PointField(name = 'y', offset = 4, datatype = PointField.FLOAT32, count = 1),
    PointField(name = 'z', offset = 8, datatype = PointField.FLOAT32, count = 1),
  ]
  msg_point_cloud.is_bigendian = False

  # Accelerometer MESSAGE
  msg_accel = Imu()
  msg_accel.header.stamp = rospy.Time.now()
  msg_accel.header.frame_id = 'accel_link'

  '''
  # GPS MESSAGE
  msg_gps = NavSatFix()
  msg_gps.header.stamp = rospy.Time.now()
  msg_gps.header.frame_id = 'gps_link'
  
  # GYRO MESSAGE
  msg_gyro = Imu()
  msg_gyro.header.stamp = rospy.Time.now()
  msg_gyro.header.frame_id = 'gyro_link'
  '''
  
  # PUBLISHERS
  pub_clock        = rospy.Publisher('/clock', Clock, queue_size=1)
  pub_camera_data  = rospy.Publisher('/camera/rgb/raw', Image, queue_size=10)
  pub_point_cloud  = rospy.Publisher('/point_cloud', PointCloud2, queue_size=10)
  pub_imu_accel  = rospy.Publisher('/accelerometer', Imu, queue_size=10)     
  pub_radar_scan  = rospy.Publisher('/frontal_radar_scan', RadarScan, queue_size=10)
  
  # pub_nav_gps   = rospy.Publisher('/gps', NavSatFix, queue_size=10)
  # pub_imu_gyro     = rospy.Publisher('/gyro', Imu, queue_size=10)

  # SUBSCRIBERS
  rospy.Subscriber('/speed'  , Float64, callback_cruise_speed  )
  rospy.Subscriber('/steering', Float64, callback_steering_angle)
  
  min_radar_range = frontal_radar_Webots.getMinRange()
  max_radar_range = frontal_radar_Webots.getMaxRange()  
  horiz_radar_fov = frontal_radar_Webots.getHorizontalFov()
  vertical_radar_fov = frontal_radar_Webots.getVerticalFov()  
  print("Min radar range=", min_radar_range, "Max radar range=", max_radar_range, "horiz_radar_fov=", horiz_radar_fov, "vertical_radar_fov=", vertical_radar_fov, sep=" ", flush=True)
  
  print("Using timestep=" + str(TIME_STEP) + " ms")
  time_lidar_last_reading  = driver.getTime()
  time_camera_last_reading = driver.getTime()
  time_accel_last_reading = driver.getTime()  
  time_radar_last_reading = driver.getTime()    
  
  while driver.step() != -1 and not rospy.is_shutdown():
    current_t = driver.getTime()
    msg_clock = Clock()
    msg_clock.clock.secs  = int(current_t)
    msg_clock.clock.nsecs = int(round(1000 * (current_t - msg_clock.clock.secs)) * 1.0e+6)
    pub_clock.publish(msg_clock)
    
    if (current_t - time_lidar_last_reading) >= 0.085:
      time_lidar_last_reading = current_t # Lidar readings are published every 100 ms
      msg_point_cloud.data = lidar.getPointCloud(data_type='buffer') # Get point cloud from lidar
      msg_point_cloud.header.stamp = rospy.Time.now() # Stamp the current lidar reading
      pub_point_cloud.publish(msg_point_cloud) # Publish point cloud ros message

    if (current_t - time_camera_last_reading) >= 0.028:
      time_camera_last_reading = current_t
      msg_image.data = camera.getImage() # Get image data from camera
      pub_camera_data.publish(msg_image) # Publish image ros message

    if (current_t - time_accel_last_reading) >= 0.01:   
      time_accel_last_reading = current_t  
      msg_accel.linear_acceleration.x = accel.getValues()[0] # GET X COMPONENT FROM Accelerometer
      msg_accel.linear_acceleration.y = accel.getValues()[1] # GET Y COMPONENT FROM Accelerometer
      msg_accel.linear_acceleration.z = accel.getValues()[2] # GET Z COMPONENT FROM Accelerometer
      pub_imu_accel.publish(msg_accel) # PUBLISHING IMU MESSAGE
    
    if (current_t - time_radar_last_reading) >= 0.001:  
      radar_returns = frontal_radar_Webots.getTargets() # from Webots
      
      radar_scan = RadarScan()
      for i, radar_target in enumerate(radar_returns):
         radar_return = RadarReturn()
         radar_return.doppler_velocity = radar_target.speed
         radar_return.range = radar_target.distance
         radar_return.amplitude = radar_target.received_power
         radar_return.azimuth = radar_target.azimuth
         radar_return.elevation = float("inf")
         radar_scan.returns.append(radar_return)         
         '''
         print("Target=", i, 
          "Doppler_velocity=", radar_scan.returns[i].doppler_velocity,
          "Range=", radar_scan.returns[i].range, 
          "Amplitude=", radar_scan.returns[i].amplitude, 
          "Azimuth=", radar_scan.returns[i].azimuth, 
          sep=" ", flush=True)
         '''        
      pub_radar_scan.publish(radar_scan) # PUBLISHING RADAR MESSAGE
            
    rate.sleep()
    
 
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
