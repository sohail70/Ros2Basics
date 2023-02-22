import rclpy
from rclpy.node import Node



def main(args=None):
    rclpy.init(args=args)
    print("Hello this is soheil coding in rclpy client library")
    rclpy.shutdown()



if __name__=='__main__':
    main()