// for debugging use --> https://gist.github.com/JADC362/a4425c2d05cdaadaaa71b697b674425f
/*
ros2 run --prefix 'gdbserver localhost:3000' af_obstacle_avoidance_cpp avoidance  --> use this to create a gdbserver 
and then use the play button in the debugger section after you created the launch.json for vs code
*/
// colcon build --packages-select <pkg_name> --cmake-args -DCMAKE_BUILD_TYPE=Debug

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
        vel_ = std::make_shared<geometry_msgs::msg::Twist>(); // If you forget to initialize then you process will die when you launch the launch file!
        scan_ = std::make_shared<sensor_msgs::msg::LaserScan>();
    }

    private:
        void timerCallback()
        {
            pub_->publish(*vel_); //if you don't initialize velocity in the constructur you'll recieve this error-->failed to publish message: ros_message argument is null
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
            if(scan_->ranges[0] > 1.0)
            {
                vel_->linear.x = 0.2;
                vel_->angular.z = 0.0;
            }
            if(scan_->ranges[0] < 1.0)
            {
                vel_->linear.x = 0.05;
                vel_->angular.z = 0.1;
            }    
            if(scan_->ranges[270] < 1.0)
            {
                vel_->linear.x = 0.05;
                vel_->angular.z = 0.1;
            }
            if (scan_->ranges[90] < 1.0)
            {
                vel_->linear.x = 0.05;
                vel_->angular.z = -0.1;
            }
            if (scan_->ranges[0] <0.3)
            {
                vel_->linear.x = 0.0;
                vel_->angular.z = 0.2;
            }
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

    rclcpp::shutdown(); 
    return 0;
}

