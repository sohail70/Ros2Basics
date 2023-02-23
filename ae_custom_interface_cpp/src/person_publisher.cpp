#include<rclcpp/rclcpp.hpp>
#include<ae_custom_interface_cpp/msg/person.hpp>
#include<chrono>

using namespace std::chrono_literals;

class CustomPub: public rclcpp::Node
{
    public:
        CustomPub():Node("CustomMsgPublisherNode")
        {
            pub_ = this->create_publisher<ae_custom_interface_cpp::msg::Person>("/person" , 10 );
            timer_ = this->create_wall_timer(500ms , std::bind(&CustomPub::TimerCallback , this));
        }
    private:
        void TimerCallback()
        {
            person_.age = 30;
            person_.name = std::string("Soheil");
            pub_->publish(person_);

        }
        ae_custom_interface_cpp::msg::Person person_;
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<ae_custom_interface_cpp::msg::Person>::SharedPtr pub_;
};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<CustomPub>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}