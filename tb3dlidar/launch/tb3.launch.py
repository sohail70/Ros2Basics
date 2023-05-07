from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command
from ament_index_python import get_package_share_directory
import os 
import random

def generate_launch_description():
  
    args =  DeclareLaunchArgument("world" ,default_value= os.path.join(get_package_share_directory("tb3dlidar") ,"worlds" , "Final.world.xml"))
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource( os.path.join(get_package_share_directory("gazebo_ros") ,"launch" , "gazebo.launch.py")))
    rob_desc = os.path.join(get_package_share_directory("tb3dlidar"),"model" , "my_tb3.urdf.xacro" )
    robot_state_publihser = Node(package="robot_state_publisher" , executable="robot_state_publisher" , name="robot_state_publisher" , output="screen",
                                 parameters=[{'robot_description': Command(["xacro " , rob_desc])}] 
                                )
    spawn_robot = Node(package="gazebo_ros" , executable="spawn_entity.py" , name="spwan_tb3" , output="screen",
                        arguments=[
                            '-topic' , 'robot_description' ,
                            '-entity' , "tb3_"+str(random.random()*10000) , 
                            "-x" , "0.0" , "-y" , "0.0" , "-z" , "0.0",
                            "-R" , "0.0" , "-P" , "0.0" , "-Y" , "0.0"
                        ])

    ld = LaunchDescription()
    ld.add_action(args)
    ld.add_action(gazebo)
    ld.add_action(robot_state_publihser)
    ld.add_action(spawn_robot)

    return ld