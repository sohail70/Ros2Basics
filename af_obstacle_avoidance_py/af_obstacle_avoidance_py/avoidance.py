import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile , ReliabilityPolicy


class Avoidance(Node):
    def __init__(self):
        super().__init__("Avoidance_node")
        self.pub_ = self.create_publisher(Twist , "cmd_vel" , 10)
        qos_profile = QoSProfile(reliability = ReliabilityPolicy.BEST_EFFORT , depth=10) # you can look up why I wrote reliability and depth inside QosProfile class 
        self.sub_ = self.create_subscription(LaserScan , "scan" , self.scan_callback ,qos_profile = qos_profile )
        self.timer_ = self.create_timer(0.2 , self.timer_callback)
        self.scan_= LaserScan()
        self.vel_ = Twist()
    
    def timer_callback(self):
        self.pub_.publish(self.vel_)

    def scan_callback(self , msg):
        self.scan_ = msg
        # self.get_logger().info("%s" %str(self.scan_.ranges[0]))
        self.process() 

    def process(self):
        if self.scan_.ranges[0] > 1.0:
            self.vel_.linear.x = 0.2
            self.vel_.angular.z = 0.0
        if self.scan_.ranges[0] < 1.0:
            self.vel_.linear.x = 0.05
            self.vel_.angular.z = 0.1
        if self.scan_.ranges[270] < 1.0:
            self.vel_.linear.x = 0.05
            self.vel_.angular.z = 0.1
        if self.scan_.ranges[90] < 1.0:
            self.vel_.linear.x = 0.05
            self.vel_.angular.z = -0.1
        if self.scan_.ranges[0] < 0.3:
            self.vel_.linear.x = 0.0
            self.vel_.angular.z = 0.2


def main(args=None):
    rclpy.init(args=args)
    node = Avoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__=='__main__':
    main()