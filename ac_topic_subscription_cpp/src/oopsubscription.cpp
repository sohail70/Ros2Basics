#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/int32.hpp>
#include<geometry_msgs/msg/twist.hpp>


class Subscription: public rclcpp::Node
{
    public:
        Subscription():Node("Subscription")
        {
            sub_ = this->create_subscription<std_msgs::msg::Int32>("/counter",10, std::bind(&Subscription::IntCallback , this , std::placeholders::_1));
            sub2_ = this->create_subscription<geometry_msgs::msg::Twist>("/cmd_vel" , 10 , std::bind(&Subscription::TwistCallback , this , std::placeholders::_1));
        }


    private:
        void IntCallback(const std_msgs::msg::Int32::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger() , "Hey: " , msg->data);
        }

        void TwistCallback(const geometry_msgs::msg::Twist::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger() , "linear_x: " , msg->linear.x , " angular_z: ",msg->angular.z );
        }

        rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr sub_;
        rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub2_;
};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv); 
    auto node = std::make_shared<Subscription>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0 ;
}
