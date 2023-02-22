#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/int32.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<chrono>
/*  
    Advantage of using timer instead a while loop:
    With a timer, if your code takes longer than the timeout, it will still be called again anyway in a new thread. 
    Using rate.sleep(), the next iteration will not start until the previous one has finished, 
    and a warning will be issued saying the loop has missed its desired rate.
*/
using namespace std::chrono_literals;

class Publisher: public rclcpp::Node
{
    public:
        Publisher(): Node("publisher") , counter(0)
        {
            pub_ =  this->create_publisher<std_msgs::msg::Int32>("/counter",10);
            pub2_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel",10);
            timer_ = this->create_wall_timer(500ms , std::bind(&Publisher::timer_callback , this));
        }
    private:

        void timer_callback()
        {
            auto msg = std_msgs::msg::Int32();
            msg.data = counter;
            counter++;

            auto msg2 = geometry_msgs::msg::Twist();
            msg2.linear.x = 0.5;
            msg2.angular.z = 0.1;

            pub_->publish(msg);
            pub2_->publish(msg2);
        }
        size_t counter;
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr pub_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub2_;
        

};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    rclcpp::spin(std::make_shared<Publisher>());
    rclcpp::shutdown();
    return 0;
}