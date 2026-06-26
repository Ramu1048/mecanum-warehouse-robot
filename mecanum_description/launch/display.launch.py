import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_description = get_package_share_directory('mecanum_description')

    xacro_file = os.path.join(pkg_description, 'urdf', 'mecanum_robot.urdf.xacro')
    rviz_config = os.path.join(pkg_description, 'rviz', 'display.rviz')

    use_sim_time = LaunchConfiguration('use_sim_time')

    # Process xacro to URDF
    robot_description = Command(['xacro ', xacro_file])

    # Declare launch arguments
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )

    # Robot State Publisher (publishes robot_description and TF)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': use_sim_time,
        }],
        output='screen'
    )

    # RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        use_sim_time_arg,
        robot_state_publisher_node,
        rviz_node,
    ])
