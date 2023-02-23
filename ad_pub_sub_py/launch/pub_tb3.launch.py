# Remember to run turtlebot3_gazebo empty_world.launch.py and add a wall to it and move the wall and play with it
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([launch_ros.actions.Node(package='ad_pub_sub_py' , executable='pubsub' , output="screen")])