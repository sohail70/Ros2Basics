#include<rclcpp/rclcpp.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<sensor_msgs/msg/laser_scan.hpp>
#include<chrono>

using namespace std::chrono_literals;

class Avoidance : public rclcpp::Node
{
    public:
    Avoidance(): Node("avoidance_node")
    {
        pub_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel" , 10);
        auto qos_profile = rclcpp::QoS(10);
        qos_profile.best_effort();
        sub_ = this->create_subscription<sensor_msgs::msg::LaserScan>("scan" , qos_profile , std::bind(&Avoidance::sensorCallback , this ,std::placeholders::_1 ));
        timer_ = this->create_wall_timer(500ms , std::bind(&Avoidance::timerCallback,this));
    }

    private:
        void timerCallback()
        {

        }
        void sensorCallback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
        {
            scan_ = msg;
            RCLCPP_INFO(this->get_logger() , "# of data %i" , msg->ranges.size() );
            RCLCPP_INFO(this->get_logger() , "Range info [0:%f pi/2:%f pi:%f 3pi/2:%f]" , scan_->ranges[0] , scan_->ranges[90] , scan_->ranges[180] ,scan_->ranges[270]);
            process();
        }

        void process()
        {
         
        }

        geometry_msgs::msg::Twist::SharedPtr vel_;
        sensor_msgs::msg::LaserScan::SharedPtr scan_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
        rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sub_;
        rclcpp::TimerBase::SharedPtr timer_;
};




int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<Avoidance>();
    rclcpp::spin(node);

}