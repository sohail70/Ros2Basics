import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
# import the LaserScan module from sensor_msgs interface
from sensor_msgs.msg import LaserScan
# import Quality of Service library, to set the correct profile and reliability in order to read sensor data.
from rclpy.qos import ReliabilityPolicy , QoSProfile #https://docs.ros2.org/latest/api/rclpy/api/qos.html

class Subscription(Node):
    def __init__(self):
        super().__init__('Subscription')
        self.sub_ = self.create_subscription(Int32 , "counter" , self.IntCallback , QoSProfile(depth=10 , reliability = ReliabilityPolicy.BEST_EFFORT))
        self.sub2_ = self.create_subscription(Twist ,"cmd_vel" ,self.TwistCallback , QoSProfile(depth=10 , reliability = ReliabilityPolicy.BEST_EFFORT))
        self.sub3_ = self.create_subscription(Odometry , "odom", self.OdomCallback , QoSProfile(depth=10 , reliability = ReliabilityPolicy.BEST_EFFORT))
        self.sub4_ = self.create_subscription(LaserScan ,"scan" ,  self.LaserCallback, QoSProfile(depth=10 , reliability = ReliabilityPolicy.BEST_EFFORT)) #is the most used to read LaserScan data and some sensor data too.
        
        self.sub_ # prevent unused variable warning
        self.sub2_ # prevent unused variable warning
        self.sub3_ # prevent unused variable warning
        self.sub4_ # prevent unused variable warning

        # define the variable to save the received info
        self.laser_data = 0

    def IntCallback(self , msg):
        self.get_logger().info("IntCallback: '%s'" % str(msg))
        
    def TwistCallback(self , msg):        
        self.get_logger().info("TwistCallback: linear=[%f , %f ,  %f]   "  %(msg.linear.x , msg.linear.y , msg.linear.z) )

    def OdomCallback(self , msg):
        self.get_logger().info("OdomCallback: '%s'  "  %str(msg))

    def LaserCallback(self , msg):
        self.get_logger().info("LaserCallback: '%s'  "  %str(msg))
        # save the received data
        self.laser_data = msg.ranges[0]
        # print the received data
        print(self.laser_data)


def main(args=None):
    rclpy.init(args=args)
    node = Subscription()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__init__':
    main()