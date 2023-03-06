from launch import LaunchDescription
from launch_ros.actions import Node




def generate_launch_description():
    server = Node(package="ag_service_cpp" , executable="server" , name="server" , output="screen")
    ld = LaunchDescription()
    ld.add_action(server)
    return ld