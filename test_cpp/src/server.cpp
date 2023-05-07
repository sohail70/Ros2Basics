#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>


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