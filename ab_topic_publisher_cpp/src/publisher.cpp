#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/int32.hpp>

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = rclcpp::Node::make_shared("publisher");
    auto publisher = node->create_publisher<std_msgs::msg::Int32>("/counter",10);
    auto msg = std::make_shared<std_msgs::msg::Int32>();
    msg->data = 0;
    
    rclcpp::WallRate loop_rate(2);
    while(rclcpp::ok())
    {
        publisher->publish(*msg);
        rclcpp::spin_some(node);
        msg->data += 1;
        loop_rate.sleep();
    }
    rclcpp::shutdown();
    return 0;
}