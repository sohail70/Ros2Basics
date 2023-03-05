from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription , DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
import os




def generate_launch_description():
    ## Gazebo 
    args = DeclareLaunchArgument("world" ,default_value= os.path.join(get_package_share_directory("af_obstacle_avoidance_py"),"worlds","wall.world.xml"))  # because gzserver.launch.py needs the world argument
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"),"launch" , "gazebo.launch.py"))
        ) 


    ## Robot State Publisher



    ## Spawn 


    ## My nodes
    avoidance = Node(package="af_obstacle_avoidance_py" , executable="avoidance" , name="avoidance" , output="screen")

    ld = LaunchDescription()
    ld.add_action(args)
    ld.add_action(gazebo)
    ld.add_action(avoidance)

    return ld