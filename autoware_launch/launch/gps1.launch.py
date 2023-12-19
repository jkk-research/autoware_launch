from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
"""
orientation_source can be gps / odom  
- gps: orientation provided from the default gps modules 
- odom: orientation counted from previous positions        
z_coord_ref_switch can be zero / exact / zero_based / orig 
- zero: the Z coordinate is always 0
- exact: the Z coorindinate is always z_coord_exact_height param (must be set in this launch)
- zero_based: Z coordinate starts from 0 and relative
- orig: the original Z provided by Duro / Piksi
euler_based_orientation:
- true: euler based, not enabled by default, please enable SPB message SBP_MSG_ORIENT_EULER 0x0221 decimal 545
- false: quaternion based, not enabled by default, please enable SPB message SBP_MSG_ORIENT_QUAT 0x0220 decimal 544
"""
# -697237.0 -5285644.0 map_gyor_0
# -639770.0 -5195040.0 map_zala_0

def generate_launch_description():
    namespace_lx = "lexus3"
    node_id = "/gps/duro"
    
    location_arg = DeclareLaunchArgument('location', default_value='gyor', description='Location name')
    location = LaunchConfiguration('location')
 
    x_coord_offset = PythonExpression(['-639770.0 if "', location, '" == "zala" else -697237.0'])
    y_coord_offset = PythonExpression(['-5195040.0 if "', location, '" == "zala" else -5285644.0'])

    duro_node = Node(
        package="duro_gps_driver",
        executable="duro_node",
        parameters=[
            {"ip_address": "192.168.10.10"},
            {"port": 55555},
            {"gps_receiver_frame_id": namespace_lx + "duro"},
            {"imu_frame_id": namespace_lx + "duro_gps_imu"},
            {"utm_frame_id": "map"},
            {"orientation_source": "gps"},
            {"x_coord_offset": x_coord_offset},
            {"y_coord_offset": y_coord_offset},
            {"z_coord_ref_switch": "exact"},
            {"z_coord_exact_height": 1.8},
            {"tf_frame_id": "map"},
            {"zero_based_pose": False},
            {"tf_child_frame_id": "lexus3/gps"},
            {"euler_based_orientation": True}           
        ],
        namespace=namespace_lx + node_id,
    )

    Node(
            # ros2 run tf2_ros static_transform_publisher -1.542 -0.49 -1.479 0.0 0.0 0.0 1.0 gps1 base_link
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['-1.542', '-0.49', '-1.479','0', '0', '0', '1','gps1','base_link'],
        ),
    
    return LaunchDescription([
        location_arg,
        duro_node
    ])