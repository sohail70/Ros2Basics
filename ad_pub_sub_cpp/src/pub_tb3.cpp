#include<rclcpp/rclcpp.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<sensor_msgs/msg/laser_scan.hpp>
#include<chrono>

using namespace std::chrono_literals;

class MoveTb3: public rclcpp::Node
{
    public:
        MoveTb3(): Node("MoveNode")
        {
            pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel" , 10);
            sub_ = this->create_subscription<sensor_msgs::msg::LaserScan>("/scan" , 10,std::bind(&MoveTb3::ScanCallback , this , std::placeholders::_1));
            timer_ = this->create_wall_timer(500ms , std::bind(&MoveTb3::TimerCallback , this));
        }
    private:
        void ScanCallback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger() , "[0:%f , pi/2: %f ,pi: %f , 3pi/2: %f]" , msg->ranges[0] , msg->ranges[90] , msg->ranges[180] , msg->ranges[270]);
            laser_data = *msg;
        }

        void TimerCallback()
        {
            if (!laser_data.ranges.empty())
            {
                if (laser_data.ranges[0]>0.5)
                {
                    vel.linear.x = 0.1;
                    pub_->publish(vel);
                }
                else
                {
                    vel.linear.x = 0.0;
                    pub_->publish(vel);
                }
            }
        }

        geometry_msgs::msg::Twist vel;
        sensor_msgs::msg::LaserScan laser_data;
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
        rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sub_;
};




int main(int argc , char* argv[])
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<MoveTb3>();
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;

}