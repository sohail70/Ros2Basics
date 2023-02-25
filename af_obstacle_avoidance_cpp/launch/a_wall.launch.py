from launch import LaunchDescription
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

from launch_ros.actions import Node

import os


def generate_launch_description():
    
    world = os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp") , 'worlds' , 'wall.world.xml')
    # print("HIIIIIIII"+str(world))
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    gazebo_server = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros , 'launch' , 'gzserver.launch.py')) , launch_arguments = {'world' : world}.items())
    gazebo_client = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros , 'launch' , 'gzclient.launch.py')))
    return LaunchDescription([
        gazebo_server,
        gazebo_client
    ])
        
    