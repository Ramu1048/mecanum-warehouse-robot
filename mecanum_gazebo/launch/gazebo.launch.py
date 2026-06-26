import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_mecanum_gazebo = get_package_share_directory('mecanum_gazebo')
    pkg_mecanum_description = get_package_share_directory('mecanum_description')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    world_file = os.path.join(pkg_mecanum_gazebo, 'worlds', 'warehouse.world')
    xacro_file = os.path.join(pkg_mecanum_description, 'urdf', 'mecanum_robot.urdf.xacro')

    # Process xacro to URDF
    robot_description = Command(['xacro ', xacro_file])

    # Declare launch arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value=world_file,
        description='Path to the Gazebo world file'
    )

    x_arg = DeclareLaunchArgument('x', default_value='0.0', description='X spawn position')
    y_arg = DeclareLaunchArgument('y', default_value='0.0', description='Y spawn position')
    z_arg = DeclareLaunchArgument('z', default_value='0.05', description='Z spawn position')

    # Include gazebo_ros launch (starts Gazebo server + client)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': LaunchConfiguration('world')}.items()
    )

    # Robot State Publisher (publishes /robot_description and TF)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True,
        }],
        output='screen'
    )

    # Spawn the robot entity in Gazebo using spawn_entity.py
    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'mecanum_robot',
            '-x', LaunchConfiguration('x'),
            '-y', LaunchConfiguration('y'),
            '-z', LaunchConfiguration('z'),
        ],
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        x_arg,
        y_arg,
        z_arg,
        gazebo,
        robot_state_publisher_node,
        spawn_entity_node,
    ])
