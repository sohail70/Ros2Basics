from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription , DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command , LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python import get_package_share_directory
import os
import random

import xacro





def generate_launch_description():
    robot_desc_path  = os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp") , "model" , "robot.urdf")
    ## Robot state publisher node
    robot_state_publisher_node = Node(package="robot_state_publisher" , executable="robot_state_publisher" , name="robot_state_publisher" ,
                                      emulate_tty=True  , parameters=[{'use_sim_time': True , 'robot_description': ParameterValue (Command(['xacro ' ,str(robot_desc_path)]),value_type=str)}] , output="screen")


    ld = LaunchDescription()

    ld.add_action(robot_state_publisher_node)

    return ld    
