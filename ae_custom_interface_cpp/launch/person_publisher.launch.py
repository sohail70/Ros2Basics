# 
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([launch_ros.actions.Node(package='ae_custom_interface_cpp' , executable='person_publisher' , output='screen')])