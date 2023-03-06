// Use services when your program doesn't require to be executed contiuously (That's the job of topics and they work with continuous flows of data)
/*
ros2 service list: Lists all the services currently running in the system --> don't confuse it with ros2 interface list package because  interface list is offline 
ros2 service call: Calls a certain service currently available
ros2 interface list: Lists all the Service messages available
ros2 interface package: Lists all the service messages from a package ---> ros2 interface package gazebo_msgs  --> # List all the messages defined in a certain package
ros2 interface packages: Lists all the available packages that have service messages defined inside them.
ros2 interface show: Gets the structure of a certain service message ---> ros2 interface show gazebo_msgs/srv/DeleteModel --> Note that -->the DeleteModel message has been substituted in ROS2 by the DelteEntity message.


ros2 interface list | grep srv ---> list all available service messages in the system

service messages .srv --> it has two part:

REQUEST (HOW you will do a call)
--- 
RESPONSE (HOW your service will respond after completing its functionality)



topic messages .msg  -> one part
*/
#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>
#include<chrono>

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = rclcpp::Node::make_shared("empty_service_client_node");
    auto client = node->create_client<std_srvs::srv::Empty>("my_service");
    auto request = std::make_shared<std_srvs::srv::Empty::Request>();
    
    while(!client->wait_for_service(std::chrono::seconds(1)))
    {
        if(!rclcpp::ok())
        {
            RCLCPP_INFO(node->get_logger(),"Interrupted while waiting for the service");
            return 0;
        }
        RCLCPP_INFO(node->get_logger() , "Waiting for the service");
    }

    auto result = client->async_send_request(request);
    if(rclcpp::spin_until_future_complete(node,result) == rclcpp::executor::FutureReturnCode::SUCCESS)
    {
        RCLCPP_INFO(node->get_logger(),"Client requested successfully");
        
    }
    else
    {
        RCLCPP_ERROR(node->get_logger() , "service call failed");
    }

    rclcpp::shutdown();
    return 0;

}