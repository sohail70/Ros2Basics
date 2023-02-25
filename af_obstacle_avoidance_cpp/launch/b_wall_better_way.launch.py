# grep -r "DeclareLaunchArgument" /opt/ros/foxy/share/ | grep import (or from!) ---> if you want to know what module has this class you can use this command

from launch import LaunchDescription
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
import os




def generate_launch_description():
    world =  os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp"), "worlds" , "wall.world.xml")
    pkg_gazebo_ros = get_package_share_directory("gazebo_ros")
    ## First way with defining args
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros,"launch" , "gazebo.launch.py")))
    args = DeclareLaunchArgument('world' , default_value=world , description="SDF World File")
    print(os.environ)
    ## Second way without defining an arg
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros,"launch" , "gazebo.launch.py")), launch_arguments={'world':world}.items())


    return LaunchDescription([
        args,
        gazebo
    ])