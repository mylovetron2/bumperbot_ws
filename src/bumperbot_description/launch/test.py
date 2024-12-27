from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'bumperbot_description'

    pkg_share = get_package_share_directory(package_name)

    urdf_file_path = os.path.join(pkg_share, 'urdf', 'bumperbot.urdf.xacro')

    with open(urdf_file_path, 'r') as urdf_file:
        robot_description = urdf_file.read()

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[{'robot_description': robot_description}],
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose'], 
        output='screen'
    )

    return LaunchDescription([
        rviz_node,
        robot_state_publisher,
        joint_state_publisher_gui,
        gazebo
    ])