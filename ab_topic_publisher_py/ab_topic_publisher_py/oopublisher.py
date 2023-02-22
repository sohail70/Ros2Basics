import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
from std_msgs.msg import Int32
# import the Twist module from geometry_msgs interface
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        # Here we have the class constructor
        # call super() in the constructor in order to initialize the Node object
        # the parameter we pass is the node name
        super().__init__('Publisher')
        self.pub_ = self.create_publisher(Int32, "counter",10)
        # create the publisher object
        # in this case the publisher will publish on /cmd_vel topic with a queue size of 10 messages.
        # use the Twist module for /cmd_vel topic
        self.pub2_ = self.create_publisher(Twist , "cmd_vel" , 10)
        # create a timer sending two parameters:
        # - the duration between 2 callbacks (0.5 seeconds)
        # - the timer function (timer_callback)
        self.create_timer(0.2 , self.timer_callback)
        self.create_timer(0.5 , self.timer_callback_2)
        self.counter = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.counter += 1
        self.pub_.publish(msg)
        self.get_logger().info( 'Published "%s" ' % msg )
    
    def timer_callback_2(self):
        # Here we have the callback method
        # create a Twist message
        msg = Twist()
        # define the linear x-axis velocity of /cmd_vel topic paramater to 0.2
        msg.linear.x  = 0.2
        # define the angular z-axis velocity of /cmd_vel topic paramater to 0.1
        msg.angular.z = 0.1
        # Publish the message to the topic
        self.pub2_.publish(msg)
        # Display the message on the console
        self.get_logger().info('Published "%s"' %msg) 




def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    publisherNode = Publisher()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(publisherNode)
    # Explicity destroy the node
    publisherNode.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()



if __name__=='__main__':
    main()