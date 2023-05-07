#include<rclcpp/rclcpp.hpp>
#include<std_srvs/srv/empty.hpp>
#include<chrono>

class Client: public rclcpp::Node
{
    public:
        Client():Node("Clier")
        {
            client_ = this->create_client<std_srvs::srv::Empty>("/My");
            // req_ = std_srvs::srv::Empty::Request::SharedPtr(); //DANGER--> THIS IS WRONG, IT DOESN'T EVEN CREATE A SHAREDPTR!
            req_ = std::make_shared<std_srvs::srv::Empty::Request>();
            call(); //in square_server client pkg I could'nt use this in the construtor but I can do this here now, weird?!!
        }
        void call()
        {
            while(! client_->wait_for_service(std::chrono::seconds(1)))
            {
                if(!rclcpp::ok())
                {
                    RCLCPP_INFO(this->get_logger() , "Interupted while waiting for the server");
                    return;
                }
                RCLCPP_INFO(this->get_logger() , "Waiting for the service");
            }
            auto result =client_->async_send_request(req_);
            if(rclcpp::spin_until_future_complete(shared_from_this(),result) == rclcpp::executor::FutureReturnCode::SUCCESS )
            {
                RCLCPP_INFO(this->get_logger() , "req succ");
            }
            else
            {
                RCLCPP_INFO(this->get_logger() , "serv call failed");
            }

        }
    private:
        rclcpp::Client<std_srvs::srv::Empty>::SharedPtr client_;
        std_srvs::srv::Empty::Request::SharedPtr req_;
};
int main(int argc, char* argv[])
{
    rclcpp::init(argc , argv);
    auto node = std::make_shared<Client>();
    // node->call();
    rclcpp::spin_some(node);
    rclcpp::shutdown();
    return 0;
    
}