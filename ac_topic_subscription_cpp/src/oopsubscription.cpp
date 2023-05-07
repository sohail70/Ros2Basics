#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/int32.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<nav_msgs/msg/odometry.hpp>

class Subscription: public rclcpp::Node
{
    public:
        // Initiate a Node called Subscription
        Subscription():Node("Subscription")
        {
            // Create a Subscriber object that will listen to the /counter topic and will call the 'topic_callback' function each time it reads something
            //10 is the subscription queue size. you can also create a qos_profile variable and create Qos object and pass it in instead of just one number!
            sub_ = this->create_subscription<std_msgs::msg::Int32>("/counter",10, std::bind(&Subscription::IntCallback , this , std::placeholders::_1)); 
            sub2_ = this->create_subscription<geometry_msgs::msg::Twist>("/cmd_vel" , 10 , std::bind(&Subscription::TwistCallback , this , std::placeholders::_1));
            sub3_ = this->create_subscription<nav_msgs::msg::Odometry>("/odom" , 10 , std::bind(&Subscription::OdomCallback ,this , std::placeholders::_1 ));
        }


    private:
        // Define a function called 'topic_callback' that receives a parameter named 'msg'
        void IntCallback(const std_msgs::msg::Int32::SharedPtr msg)
        {
            // Print the value 'data' inside the 'msg' parameter
            RCLCPP_INFO(this->get_logger() , "Hey: '%d'" , msg->data);
        }

        void TwistCallback(const geometry_msgs::msg::Twist::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger() , "linear_x: %f  , angular_z: %f ", msg->linear.x ,msg->angular.z );
        }

        void OdomCallback(const nav_msgs::msg::Odometry::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger() , "x: %f ,y: %f ,z: %f", msg->pose.pose.position.x , msg->pose.pose.position.y , msg->pose.pose.position.z);
        }

        rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr sub_;
        rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub2_;
        rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr sub3_;
};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv); 
    auto node = std::make_shared<Subscription>();
    // Create a loop that will keep the program in execution
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0 ;
}
