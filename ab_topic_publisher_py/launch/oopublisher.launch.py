from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([launch_ros.actions.Node(package='ab_topic_publisher_py' , executable='oopublisher' , output='screen')])