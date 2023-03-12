cmake_minimum_required(VERSION 3.5)
project(ah_square_service_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(gazebo_msgs REQUIRED)

#############################
# For Message Generation 
find_package(rosidl_default_generators REQUIRED) #rosidl_default_generators is in charge of generating new interfaces in ROS2
rosidl_generate_interfaces(${PROJECT_NAME} "srv/MyCustomServiceMessage.srv") # rosidl_generate_interface function is gor generating the new service interface


# For my current package to use it
find_package(ah_square_service_cpp REQUIRED) # looks a bit weird because this is the package that also has the message but i wrote it for completion --> you also have to put this pkg name in ament_target_dependencies

############################$

add_executable(square_server src/square_service_server.cpp)
add_executable(square_client src/square_service_client.cpp)


ament_target_dependencies(square_server rclcpp std_msgs std_srvs gazebo_msgs ah_square_service_cpp)
ament_target_dependencies(square_client rclcpp std_msgs std_srvs gazebo_msgs ah_square_service_cpp)

install(TARGETS square_server square_client DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY launch model worlds DESTINATION share/${PROJECT_NAME})


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
