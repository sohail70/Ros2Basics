#include<rclcpp/rclcpp.hpp>

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = rclcpp::Node::make_shared("Hi");
    RCLCPP_INFO(node->get_logger() , "Hi my name is soheil");

    rclcpp::shutdown();
    return 0;
}
