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
    world =os.path.join( get_package_share_directory("af_obstacle_avoidance_cpp") , "worlds" , "wall.world.xml")
    pkg_gazebo_ros = get_package_share_directory("gazebo_ros")
    # os.environ["GAZEBO_MODEL_PATH"] = os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp") , "model" , "turtlebot3_waffle.urdf.xacro")
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros,"launch","gazebo.launch.py")))
    args = DeclareLaunchArgument('world' , default_value= world , description="World Sdf file")


    ############################## PUBLISH THE URDF FILE #################################
    # sdf_file  = os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp") , "model" , "robot.urdf")
    robot_desc_path  = os.path.join(get_package_share_directory("af_obstacle_avoidance_cpp") , "model" , "turtlebot3_waffle_pi.urdf")
    
    # sdf_model = LaunchConfiguration('sdf_model') 
    # declare_sdf_model_path_cmd = DeclareLaunchArgument(
    #   name='sdf_model', 
    #   default_value=sdf_file, 
    #   description='Absolute path to robot sdf file')
    ## Robot state publisher node
    robot_state_publisher_node = Node(package="robot_state_publisher" , executable="robot_state_publisher" , name="robot_state_publisher" ,
                                      emulate_tty=True  , parameters=[{'use_sim_time': True , 'robot_description': ParameterValue (Command(['xacro ' ,str(robot_desc_path)]),value_type=str)}] , output="screen")



    ############################## SPAWNING THE ROBOT #################################
    position = [0.0 , 0.0 , 0.0]
    orientation = [0.0 , 0.0 , 0.0] # [Roll , Pitch , Yaw] --> in radians
    robot_base_name = "tb3"
    entity_name = robot_base_name+"-"+str(int(random.random()*100000)) # just in case we want to spawn different robots

    # spawn_endtity.py gets the urdf file from the /robot_description topic and spawns it into gazebo
    # Ros2 run gazebo_ros spawn_entity.py -h -> to see what args you need or chekout the spawn_entity.py in opt to check the python file
    spawn_robot = Node(package="gazebo_ros" , executable="spawn_entity.py" , name="spawn_entity" , output = "screen" , 
                       arguments=['-entity' , entity_name , '-x' , str(position[0]) , '-y' , str(position[1]) , '-z' , str(position[2])  ,
                                  '-R' , str(orientation[0]) , '-P' , str(orientation[1])  , '-Y' , str(orientation[2]) , '-topic' , '/robot_description' ]) # The content of the URDF file should be published in this topic


    ld = LaunchDescription()
    # ld.add_action(declare_sdf_model_path_cmd)
    ld.add_action(args)
    ld.add_action(gazebo)
    ld.add_action(robot_state_publisher_node)
    # ld.add_action(spawn_robot)
    return ld    
