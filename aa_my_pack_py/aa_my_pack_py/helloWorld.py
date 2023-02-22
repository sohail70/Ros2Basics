import rclpy
from rclpy.node import Node

#Remeber python is a script and we want it in such a way that if we change the below program we didn't have to colcon build it every time so the first time you build 
#the project you should use colcon build --symlink-instal and now if you change the code and save and use ros2 launch without colcon build it will update it self!

def main(args=None):
    rclpy.init(args=args)
    print("Hello this is soheil coding in rclpy client library")
    rclpy.shutdown()



if __name__=='__main__':
    main()