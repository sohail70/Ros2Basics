#include<rclcpp/rclcpp.hpp>


int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = rclcpp::Node::make_shared("Hi");

    rclcpp::WallRate loop_rate(2);
    while(rclcpp::ok())
    {
        RCLCPP_INFO(node->get_logger() , "Hi call me soheil");
        loop_rate.sleep();
        rclcpp::spin_some(node);
    }
    rclcpp::shutdown();
    return 0; 
}