#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>

std::shared_ptr<rclcpp::Node> node = nullptr;

void service_callback(const std::shared_ptr<std_srvs::srv::Empty::Request> req , const std::shared_ptr<std_srvs::srv::Empty::Response> res)
{
    RCLCPP_INFO(node->get_logger() , "Service callback is being called");
}



int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    node = rclcpp::Node::make_shared("empty_service_server_node"); //std::make_shared<rclcpp::Node>();
    auto server = node->create_service<std_srvs::srv::Empty>("my_service" , service_callback);
    rclcpp::spin(node);
    rclcpp::shutdown();
    node = nullptr;
    return 0;

}