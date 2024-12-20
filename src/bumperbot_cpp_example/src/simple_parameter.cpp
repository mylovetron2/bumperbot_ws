#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

class SimpleParameter: public rclcpp::Node
{
    public:
        SimpleParameter(): Node("simple_parameter"){
            declare_parameter<int>("simple_int_param",28);
            declare_parameter<std::string>("simple_string_param","Antonio");

            add_on_set_parameters_callback(std::bind(SimpleParameter::paramChangeCallback,this, _1));
        }
    private:
        OnSetParameterCallbackHandle::SharedPtr param_callback_handle_;
        
}