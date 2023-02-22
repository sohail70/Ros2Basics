from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([launch_ros.actions.Node(package='aa_my_pack_py' , executable='helloWorld' , output='screen')])