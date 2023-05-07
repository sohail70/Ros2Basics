#include<rclcpp/rclcpp.hpp>
#include<test_cpp/msg/blah.hpp>
#include<chrono>

using namespace std::chrono_literals;

class Publisher: public rclcpp::Node
{
    public:
        Publisher():Node("Puber")
        {
            pub_ = this->create_publisher<test_cpp::msg::Blah>("/blah",10);
            timer_ = this->create_wall_timer(500ms , std::bind(&Publisher::TimerCallback , this));
        }

        void TimerCallback()
        {
            auto msg = test_cpp::msg::Blah();
            msg.b = true;
            msg.f = 120.5;
            msg.i = 120;

            pub_->publish(msg);
        }

    private:
        rclcpp::Publisher<test_cpp::msg::Blah>::SharedPtr pub_;
        rclcpp::TimerBase::SharedPtr timer_;
};


int main(int argc , char* argv[])
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Publisher>();
    rclcpp::spin(node);
    rclcpp::shutdown(); 
}