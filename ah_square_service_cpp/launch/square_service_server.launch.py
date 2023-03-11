from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command
from ament_index_python import get_package_share_directory
import os 


def generate_launch_description():
    ## Gazebo
    args =  DeclareLaunchArgument("world" ,default_value= os.path.join(get_package_share_directory("ah_square_service_cpp") ,"worlds" , "wall.world.xml"))
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource( os.path.join(get_package_share_directory("gazebo_ros") ,"launch" , "gazebo.launch.py")))



    ## Robot State Publisher
    rob_desc = os.path.join(get_package_share_directory("ah_square_service_cpp"),"model" , "my_tb3.urdf.xacro" )
    robot_state_publihser = Node(package="robot_state_publisher" , executable="robot_state_publisher" , name="robot_state_publisher" , output="screen",
                                 parameters=[{'robot_description': Command("xacro " , rob_desc)}] #why parameters? see the robot_state_publisher source code in github! It also uses the std::map and I think thats the reason for using key value pair
                                )


    ## Spawn tb3
    spawn_robot = Node(package="gazebo_ros" , executable="spawn_entity.py" , name="spwan_tb3" , output="screen",
                        arguments=[]
                        )

    ## My Nodes



    ld = LaunchDescription()
    ld.add_action(args)
    ld.add_action(gazebo)

    return ld