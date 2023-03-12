/*
How to debug?
colcon build --packages-select ah_square_service_cpp  --cmake-args -DCMAKE_BUILD_TYPE=Debug
change the launch.json in .vscode
ros2 run --prefix 'gdbserver localhost:3000' ah_square_service_cpp square_client
hit the play button on debug tab or use ctrl+shift+d

*/


#include<rclcpp/rclcpp.hpp>
#include<ah_square_service_cpp/srv/my_custom_service_message.hpp>



class SquareClient: public rclcpp::Node
{
    public:
        SquareClient(): Node("square_service_client_node")
        {
            // // DANGER --> you get a bad weakptr error if you put executeRequest here in the constructor because in that function I call shared_from_this() and the object is not finished creating in the constructor yet and you wanna get a sharedptr of it! it doens't work!
            // square_client_ = this->create_client<ah_square_service_cpp::srv::MyCustomServiceMessage>("square_server");
            // executeRequest();
        }
        void setupClient()
        {
            square_client_ = this->create_client<ah_square_service_cpp::srv::MyCustomServiceMessage>("square_server");
            executeRequest();
        }
    private:
        int executeRequest()
        {
            ah_square_service_cpp::srv::MyCustomServiceMessage::Request::SharedPtr req = std::make_shared<ah_square_service_cpp::srv::MyCustomServiceMessage::Request>();
            req->distance = 1.0;
            req->repititions = 1;
            
            while (!square_client_->wait_for_service(std::chrono::seconds(1)))
            {
                if(!rclcpp::ok())
                {
                    RCLCPP_INFO(this->get_logger() , "Interuppted");
                    return -1;
                }

                RCLCPP_INFO(this->get_logger() , "No server found yet!");
            }

            auto future_result = square_client_->async_send_request(req);
            
            if (rclcpp::spin_until_future_complete(shared_from_this(), future_result) != rclcpp::executor::FutureReturnCode::SUCCESS) // notice that the first arg needs a node sharedPtr so I coudln't use "this" and had to use shared_from_this() to get a shared pointer out of "this"
            {
                RCLCPP_INFO(this->get_logger() , "Service call failed");
                return -1;
            }

            auto response = future_result.get();
            RCLCPP_INFO(this->get_logger() , "Result %i" , response->success);
            return 0; 
        }
        rclcpp::Client<ah_square_service_cpp::srv::MyCustomServiceMessage>::SharedPtr square_client_;
};

int main(int argc , char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<SquareClient>();
    node->setupClient(); // This is necessary because you can't just use shared_from_this() inside the constructor
    rclcpp::spin_some(node); //It's important that you put spin_some here because the SquareClient class it self has something called spin)until_future_complete so when you get the result ros shutsdown but if you use spin it doesn't
    rclcpp::shutdown();
    return 0;
}