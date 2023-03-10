import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
# import the Twist module from geometry_msgs interface
from geometry_msgs.msg import Twist
# import the LaserScan module from sensor_msgs interface
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy , QoSProfile

class MoveTb3(Node):
    def __init__(self):
        super().__init__("move")
        self.pub_ = self.create_publisher(Twist ,"cmd_vel" ,10)
        self.sub_ = self.create_subscription(LaserScan , "scan" , self.ScanCallback,  QoSProfile(reliability = ReliabilityPolicy.BEST_EFFORT , depth = 10) )
        self.sub_
        self.laserData = LaserScan()
        self.create_timer(0.1 , self.timer_callback)

    def ScanCallback(self ,msg):
        self.get_logger().info("many?? %i" % len(msg.ranges))
        # self.get_logger().info("ranges[0] , ranges[pi/2] , ranges [pi] , ranges[3pi/2] , [%s , %s , %s , %s]" %(str(msg.ranges[0]) , str(msg.ranges[360//4]) , str(msg.ranges[360//2]) , str(msg.ranges[270]))) 
        self.laserData = msg

    def timer_callback(self):
        if len(self.laserData.ranges) != 0:
            self.get_logger().info("ranges[0] , ranges[pi/2] , ranges [pi] , ranges[3pi/2] , [%s , %s , %s , %s]" %(str(self.laserData.ranges[0]) , str(self.laserData.ranges[360//4]) , str(self.laserData.ranges[360//2]) , str(self.laserData.ranges[270]))) 
            msg = Twist()
        
            if self.laserData.ranges[0]>0.5 :
                msg.linear.x = 0.1
                self.pub_.publish(msg)
            else:
                msg.linear.x = 0.0
                self.pub_.publish(msg)

       






def main(args=None):
    rclpy.init(args=args)
    node = MoveTb3()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()