from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pub_node = Node(package='test_cpp' , executable='publish' , output='screen')
    ld = LaunchDescription()
    ld.add_action(pub_node)
    return ld
