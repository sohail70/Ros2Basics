from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription , DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch.substitutions import Command
import os
import random



def generate_launch_description():
    ## Gazebo 
    args = DeclareLaunchArgument("world" ,default_value= os.path.join(get_package_share_directory("af_obstacle_avoidance_py"),"worlds","wall.world.xml"))  # because gzserver.launch.py needs the world argument
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"),"launch" , "gazebo.launch.py"))
        ) 


    ## Robot State Publisher
    robot_state_publisher = Node(package="robot_state_publisher" , executable="robot_state_publisher" , name="robot_state_publisher" , output="screen" ,
                                parameters=[{'robot_description': Command(['xacro ', os.path.join(get_package_share_directory("af_obstacle_avoidance_py"),"model","my_tb3.urdf.xacro")   ]   )}]    
                                )


    ## Spawn 
    spawn_robot = Node(package="gazebo_ros" , executable="spawn_entity.py" , name="spawn_entity" , output="screen" , 
        arguments= [
            "-entity" , "tb3"+str(int(random.random()*10000)) ,
             "-topic" , "robot_description",
             '-x' , str(0.0) , '-y' , str(0.0) , '-z' , str(0.0),
             '-R' , str(0.0) , '-P' , str(0.0) , '-Y' , str(0.0),
            ])

    ## My nodes
    avoidance = Node(package="af_obstacle_avoidance_py" , executable="avoidance" , name="avoidance" , output="screen")

    ld = LaunchDescription()
    ld.add_action(args)
    ld.add_action(gazebo)
    ld.add_action(robot_state_publisher)
    ld.add_action(spawn_robot)
    ld.add_action(avoidance)

    return ld