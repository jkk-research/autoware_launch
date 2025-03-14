from launch import LaunchDescription
from launch_ros.actions import Node
import math

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='gyor0_tf_publisher',
            output='screen',
            arguments=[
                '--x',  '697237.0',
                '--y',  '5285644.0',
                '--z',  '0.0',
                '--qx', '0.0',
                '--qy', '0.0',
                '--qz', '0.0',
                '--qw', '1.0',

                '--frame-id',      'map',
                '--child-frame-id','map_gyor_0'
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='zala0_tf_publisher',
            output='screen',
            arguments=[
                '--x',  '639770.0',
                '--y',  '5195040.0',
                '--z',  '0.0',
                '--qx', '0.0',
                '--qy', '0.0',
                '--qz', '0.0',
                '--qw', '1.0',

                '--frame-id',       'map',
                '--child-frame-id', 'map_zala_0'
            ],
        ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='left1_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '0.75',
        #         '--y',     '0.5',
        #         '--z',     '1.3',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  '0.0',
        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_left_a'
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='right1_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '1.53',
        #         '--y',     '-0.5',
        #         '--z',     '1.41',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  '0.0',

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_right_a'
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='center1_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '0.75',
        #         '--y',     '0.0',
        #         '--z',     '1.91',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  '0.0',

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_center_a'
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='center2_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '0.75',
        #         '--y',     '0.0',
        #         '--z',     '1.91',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  str(math.pi),

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_center_a_laser_data_frame'
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='left2_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '0.75',
        #         '--y',     '0.5',
        #         '--z',     '1.3',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  str(math.pi),

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_left_a_laser_data_frame'
        #     ],
        # ),  
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='right2_os_front_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',     '1.53',
        #         '--y',     '-0.5',
        #         '--z',     '1.41',
        #         '--yaw',   '0.0',
        #         '--pitch', '0.0',
        #         '--roll',  str(math.pi),

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'os_right_a_laser_data_frame'
        #     ],
        # ),

    ])