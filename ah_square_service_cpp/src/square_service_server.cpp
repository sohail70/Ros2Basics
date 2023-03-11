#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>
class SquareServer : public rclcpp::Node
{
    public:
        SquareServer():Node("square_service_server_node")
        {
            square_service = this->create_service<std_srvs::srv::Empty>("square_server" , std::bind(&SquareServer::serviceServer ,this ,std::placeholders::_1 , std::placeholders::_2));
        }

    private:
        void serviceServer(const std_srvs::srv::Empty::Request::SharedPtr req , const std_srvs::srv::Empty::Response::SharedPtr res)
        {
            RCLCPP_INFO(this->get_logger() , "Service has been called");
        }
        rclcpp::Service<std_srvs::srv::Empty>::SharedPtr square_service;
        

};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<SquareServer>();
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}