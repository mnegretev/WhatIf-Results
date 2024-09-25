# WhatIf-Results
Software to reproduce results for What-If experiments


## Requirements:

* Ubuntu 20.04
* ROS Noetic (http://wiki.ros.org/noetic/Installation/Ubuntu)
* Webots 2022a (https://github.com/cyberbotics/webots/releases/download/R2022a/webots_2022a_amd64.deb)

## Installation

Note: It is assumed that Ubuntu OS, ROS platform and Webots simulator are already installed. 

* $ cd
* $ git clone https://github.com/mnegretev/WhatIf-Results
* $ cd WhatIf-Results/catkin_ws
* $ catkin_make
* $ sudo pip3 install beepy
* $ sudo apt install ros-noetic-webots-ros
* $ sudo apt install ros-noetic-ros-numpy
* $ echo "source ~/WhatIf-Results/catkin_ws/devel/setup.bash" >> ~/.bashrc
* $ source ~/.bashrc

## Experimentos:

Carril sin cruce con cuatro obstáculo y vehículo autónomo en carril izquierdo
* $ roslaunch get_samples what_if_straight_left.launch

Carril sin cruce con cuatro obstáculo y vehículo autónomo en carril derecho
* $ roslaunch get_samples what_if_straight_right.launch

Mundo con cruce y un solo obstáculo en carril transversal:
* $ roslaunch get_samples what_if_cross.launch cross:=01

Mundo con cruce y un solo obstáculo en carril del vehículo:
* $ roslaunch get_samples what_if_cross.launch cross:=02

Mundo con cruce y dos obstáculos en carril transversal:
* $ roslaunch get_samples what_if_cross.launch cross:=03

Mundo con cruce y dos obstáculos en carril del vehículo:
* $ roslaunch get_samples what_if_cross.launch cross:=04

Mundo con cruce y cuatro obstáculos (dos en carril del vehículo y dos en transversal):
* $ roslaunch get_samples what_if_cross.launch cross:=05

Con los botones de la GUI se activan los comportamientos


## Contact

Héctor Avilés<br>
havilesa@upv.edu.mx <br>
Marco Negrete<br>
marco.negrete@ingenieria.unam.edu

