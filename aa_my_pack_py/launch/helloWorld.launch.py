from launch import LaunchDescription
import launch_ros.actions
#don't forget to chmod +x the launch files
def generate_launch_description():
    return LaunchDescription([launch_ros.actions.Node(package='aa_my_pack_py' , executable='helloWorld' , output='screen')])