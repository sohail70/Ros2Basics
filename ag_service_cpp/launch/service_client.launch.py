from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    client = Node(package="ag_service_cpp" , executable="client" , name="client" , output="screen")
    ld = LaunchDescription()
    ld.add_action(client)
    return ld