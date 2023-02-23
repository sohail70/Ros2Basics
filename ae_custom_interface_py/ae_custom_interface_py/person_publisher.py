'''
Remeber when you create this pkg you have to use --dependencies rclpy ae_custom_interface_cpp because you are using the msg that you built in that pkg

Recall that interfaces can currently only be defined in CMake packages. 
It is possible, however, to have Python libraries and nodes in CMake packages (using ament_cmake_python),
so you could define interfaces and Python nodes together in one package

Remeber when you build a message the build system creates header files as well as the python files so you can import you message in python environment too
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

def main(args=None):
    rclpy.init(args=args)
    node = CustomPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

