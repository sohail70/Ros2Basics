import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.pub_ = self.create_publisher(Int32, "counter",10)
        self.pub2_ = self.create_publisher(Twist , "cmd_vel" , 10)
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
        msg = Twist()
        msg.linear.x  = 0.2
        msg.angular.z = 0.1
        self.pub2_.publish(msg)
        self.get_logger().info('Published "%s"' %msg) 




def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=='__main__':
    main()