# ros2 launch lexus3_sensor_kit_launch imu.launch.py 
# ros2 launch autoware_launch can1.launch.xml
# ros2 launch autoware_launch tf_static.launch.py
# ros2 launch lexus_bringup os_composable_raw_merged_b_autoware.launch.py >> TODO: move to autoware_launch
# ros2 launch autoware_raw_vehicle_cmd_converter raw_vehicle_converter.launch.xml
# ros2 run autoware_speed_relay speed_relay 


import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource, FrontendLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # include launch file lexus3_sensor_kit_launch imu.launch.py 
    imu_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('lexus3_sensor_kit_launch'),
                'launch/imu.launch.py'))
    )

    # include launch file autoware_launch can1.launch.xml
    can1_include = IncludeLaunchDescription(
        FrontendLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('autoware_launch'),
                'launch/can1.launch.xml'))
    )

    # include launch file autoware_launch tf_static.launch.py
    tf_static_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('autoware_launch'),
                'launch/tf_static.launch.py'))
    )

    # TODO: move 
    # include launch file lexus_bringup os_composable_raw_merged_b_autoware.launch.py
    os_composable_raw_merged_b_autoware_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('lexus_bringup'),
                'launch/drivers/os_composable_raw_merged_b_autoware.launch.py'))
    )

    # include launch file autoware_raw_vehicle_cmd_converter raw_vehicle_converter.launch.xml
    raw_vehicle_converter_include = IncludeLaunchDescription(
        FrontendLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('autoware_raw_vehicle_cmd_converter'),
                'launch/raw_vehicle_converter.launch.xml'))
    )

    # run autoware_speed_relay
    autoware_speed_relay = Node(
        package='autoware_speed_relay',
        executable='speed_relay',
        output='screen'
    )

    return LaunchDescription([
        imu_include,
        can1_include,
        tf_static_include,
        os_composable_raw_merged_b_autoware_include,
        raw_vehicle_converter_include,
        autoware_speed_relay,
    ])