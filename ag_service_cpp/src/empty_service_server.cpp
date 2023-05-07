#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>

std::shared_ptr<rclcpp::Node> node = nullptr;
//Or use this: void service_callback(const std_srvs::srv::Empty::Request::SharedPtr req , const std_srvs::srv::Empty::Response::SharedPtr res)
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



/*
//using a class for server

class Server : public rclcpp::Node
{
    public:
        Server():Node("server")
        {
            server_ = this->create_service<std_srvs::srv::Empty>("/My" , std::bind(&Server::Callback , this , std::placeholders::_1 , std::placeholders::_2));
        }

        void Callback(const std_srvs::srv::Empty::Request::SharedPtr req , const std_srvs::srv::Empty::Response::SharedPtr res)
        {
           RCLCPP_INFO(this->get_logger() , "Bambooooozeled") ;
        }
    private:
        rclcpp::Service<std_srvs::srv::Empty>::SharedPtr server_;        
};


int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<Server>();
    rclcpp::spin(node); 
    rclcpp::shutdown();
}



*/