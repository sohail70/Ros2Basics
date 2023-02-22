import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        #call super() in the constructor in order to initialize the Node object
        #the parameter we pass is the node name
        super().__init__('Hi')
        #create a timer sending two parameters:
        #the duration between two callbacks (0.2 seconds)
        #the timer function (timer_callback)
        self.create_timer(0.2 , self.timer_callback)
    
    def timer_callback(self):
        #print a ROS2 log on the terminal
        self.get_logger().info("Hey my name is soheil working on ROS2")


def main(args=None):
    #initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    node = MyNode()
    #pause the program execution, waits for a request to kill the node
    rclpy.spin(node)
    #shutdown the ROS communication
    rclpy.shutdown()

if __name__=='__main__':
    main()