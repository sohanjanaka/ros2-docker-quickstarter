from launch import LaunchDescription
from launch_ros.actions import Node
import xacro
import os

def generate_launch_description():

    # Process the URDF file robot.urdf.xacro 
    xacro_file = os.path.join('ros2_ws/src/my_python_package', 'urdf','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    params = {'robot_description': robot_description_config.toxml()}

    return LaunchDescription([
        Node(
            package='my_python_package',
            executable='my_node',
            name='my_node',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[params]
        ),
    ])
