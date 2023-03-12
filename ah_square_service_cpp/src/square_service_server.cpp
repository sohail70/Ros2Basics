#include<rclcpp/rclcpp.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<ah_square_service_cpp/srv/my_custom_service_message.hpp>

using  CustomReqPtr = ah_square_service_cpp::srv::MyCustomServiceMessage::Request::SharedPtr;
using  CustomResPtr = ah_square_service_cpp::srv::MyCustomServiceMessage::Response::SharedPtr;

class SquareServer : public rclcpp::Node
{
    public:
        SquareServer():Node("square_service_server_node")
        {
            square_service_ = this->create_service<ah_square_service_cpp::srv::MyCustomServiceMessage>("square_server" , std::bind(&SquareServer::serviceServer ,this ,std::placeholders::_1 , std::placeholders::_2));
            pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel" , 10);
            vel_lin_.linear.x = 0.1;
            vel_lin_.angular.z = 0.05;
            
            
        }

    private:
        void serviceServer(const CustomReqPtr req , const CustomResPtr res)
        {
            RCLCPP_INFO(this->get_logger() , "Service has been called");

            // double time_needed;
            // for(int i = 0 ; i< reps ; i++)
            // {
            //     for (int j = 0 ; j <4 ; j++)
            //     {
            //     }
            // }
              
        }


        rclcpp::Service<ah_square_service_cpp::srv::MyCustomServiceMessage>::SharedPtr square_service_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
        
        geometry_msgs::msg::Twist vel_lin_ ;
        geometry_msgs::msg::Twist vel_ang_;
        geometry_msgs::msg::Twist vel_stop_;

};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<SquareServer>();
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}