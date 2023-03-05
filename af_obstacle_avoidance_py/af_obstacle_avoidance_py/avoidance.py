import rclpy
from rclpy.node import Node




class Avoidance(Node):
    def __init__(self):
        super().__init__("Avoidance_node")
        self.get_logger().error("HELLO")



def main(args=None):
    rclpy.init(args=args)
    node = Avoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__=='__main__':
    main()