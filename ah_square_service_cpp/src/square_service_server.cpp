#include<rclcpp/rclcpp.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<ah_square_service_cpp/srv/my_custom_service_message.hpp>
#include<chrono>


// Call it by using --> ros2 service call /square_server ah_square_service_cpp/srv/MyCustomServiceMessage "{distance: 0.1 , repititions: 2}" 

using  CustomReqPtr = ah_square_service_cpp::srv::MyCustomServiceMessage::Request::SharedPtr;
using  CustomResPtr = ah_square_service_cpp::srv::MyCustomServiceMessage::Response::SharedPtr;

class SquareServer : public rclcpp::Node
{
    public:
        SquareServer():Node("square_service_server_node")
        {
            square_service_ = this->create_service<ah_square_service_cpp::srv::MyCustomServiceMessage>("square_server" , std::bind(&SquareServer::serviceServer ,this ,std::placeholders::_1 , std::placeholders::_2));
            pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel" , 10);
            
            vel_lin_.linear.x = 0.2;
            vel_lin_.angular.z = 0.0;
            
            vel_ang_.linear.x = 0.0;
            vel_ang_.angular.z = 0.1;

            vel_stop_.linear.x = 0.0;
            vel_stop_.angular.z = 0.0;
            
        }

    private:
        void serviceServer(const CustomReqPtr req , const CustomResPtr res)
        {
            RCLCPP_INFO(this->get_logger() , "Service has been called");
            double distance = req->distance;
            int repetitions = req->repititions;
            double time_needed;

            for (int i = 0 ; i <repetitions ; i++)
            {
                for (int j =  0 ; j < 4 ; j ++)
                {
                    // Staright
                    time_needed = distance / vel_lin_.linear.x ; 
                    auto sleep_duration = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::duration<double>(time_needed));
                    RCLCPP_INFO(this->get_logger(), "Nano Seconds: %s" , std::to_string(sleep_duration.count()).c_str());
                    pub_->publish(vel_lin_);
                    rclcpp::sleep_for(sleep_duration);
                    // Stop
                    pub_->publish(vel_stop_);
                    // Turn
                    time_needed = M_PI_2/vel_ang_.angular.z;
                    pub_->publish(vel_ang_);
                    sleep_duration = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::duration<double>(time_needed));
                    rclcpp::sleep_for(sleep_duration);
                    // Stop
                    pub_->publish(vel_stop_);
                }
            }

            res->success = true;

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