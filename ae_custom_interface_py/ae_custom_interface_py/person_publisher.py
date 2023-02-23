'''
Remeber when you create this pkg you have to use --dependencies rclpy ae_custom_interface_cpp because you are using the msg that you built in that pkg

Recall that interfaces can currently only be defined in CMake packages. 
It is possible, however, to have Python libraries and nodes in CMake packages (using ament_cmake_python),
so you could define interfaces and Python nodes together in one package

Remeber when you build a message the build system creates header files as well as the python files so you can import you message in python environment too


I asked chatGPT whats in ament_index folder?
The ament_index folder is a directory created by ROS 2 build system (Colcon) during the build process, 
which contains an index of all the installed packages and their resources. 
The purpose of the ament_index is to provide a way for packages to find resources in other packages. 
For example, when a ROS 2 package depends on another package that provides custom messages, 
the ament_index is used to locate the installed message package and the message files.
The ament_index folder is typically located in the install directory of a ROS 2 workspace, 
and contains a set of YAML files that describe the resources provided by each installed package, 
including messages, services, actions, and launch files. The ament_index also includes an interfaces 
subdirectory that contains the generated Python code for custom message types, as well as a set of index files 
that provide a mapping between message type names and the Python modules that define them.
The ament_index folder contains a collection of files that are used for package discovery and management in ROS 2.
Some of the files in this folder are empty by default, as they are intended to be populated with package information by 
the build system during package compilation and installation. For example, the resources.ros2-<distro>.cmake file in the 
ament_index/resource_index/ directory is empty by default, but it will be populated with the paths to the installed resources 
of each package during the build process.
Other files, such as the resource_index.yaml file in the ament_index/resource_index/ directory, may be populated 
with default values or manually edited to include package information.

and interestingly enough there is also ament_index in the local workspace in the share folder of your Ros2Basics WS. so maybe you should add the path to the setup.py 

'''

import rclpy
from rclpy.node import Node
from ae_custom_interface_cpp.msg import Person

class CustomPub(Node):
    def __init__(self):
        super().__init__("PersonPublisherNode")
        self.pub_ = self.create_publisher(Person,"/person" , 10)
        self.timer_ = self.create_timer(0.2 , self.TimerCallback)
        self.msg = Person()
        
        

    def TimerCallback(self):
        self.msg.age = 10.0
        self.msg.name = str("soheil")
        self.get_logger().info("Age %f" %self.msg.age)
        self.pub_.publish(self.msg)
    def onShutDown(self):
        self.get_logger().info("Shuting down!")


def main(args=None):
    rclpy.init(args=args)
    node = CustomPub()
    rclpy.get_default_context().on_shutdown(node.onShutDown) # pause the program execution, waits for a request to kill the node (ctrl+c)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

