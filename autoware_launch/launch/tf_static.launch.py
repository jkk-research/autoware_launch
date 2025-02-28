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
        #     name='duro_gps_tf_publisher',
        #     output='screen',
        #     arguments=[
        #         '--x',  '1.6',
        #         '--y',  '0.0',
        #         '--z',  '0.2',
        #         '--qx', '0.0',
        #         '--qy', '0.0',
        #         '--qz', '0.0',
        #         '--qw', '1.0',

        #         '--frame-id',       'base_link',
        #         '--child-frame-id', 'duro_gps'
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='base_gps_tf_publisher',
        #     output='screen',
        #     # https://raw.githubusercontent.com/wiki/szenergy/szenergy-public-resources/img/2022.L.01.svg
        #     arguments=['-1.542', '-0.49', '-1.479', '0.0', '0', '0', namespace + '/' + 'gps', namespace + '/' + 'base_link'], # TODO
        # ),
        # 1.5 deg to rad =  0.0261799
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='zed_camera_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',  '1.6',
                '--y',  '0.0',
                '--z',  '1.286',
                '--qx', '0.0',
                '--qy', '0.0',
                '--qz', '0.0',
                '--qw', '1.0',

                '--frame-id',       'base_link',
                '--child-frame-id', '_left_camera_frame'
            ],
        ),
        # Node(
        #     package='tf2_ros',
        #     #namespace='lexus3',
        #     executable='static_transform_publisher',
        #     name='duro_gps_imu_tf_publisher',
        #     output='screen',
        #     arguments=['0.0', '0.0', '0.2','0', '0', '0', '1', 'base_link', namespace + '/' + 'duro_gps_imu'],
        # ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_ground_link_publisher',
            output='screen',
            arguments=[
                '--x',  '0.0',
                '--y',  '0.0',
                '--z',  '-0.37',
                '--qx', '0.0',
                '--qy', '0.0',
                '--qz', '0.0',
                '--qw', '1.0',
                
                '--frame-id',       'base_link',
                '--child-frame-id', 'ground_link'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='left1_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '0.75',
                '--y',     '0.5',
                '--z',     '1.3',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  '0.0',

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_left_a'
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='right1_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '1.53',
                '--y',     '-0.5',
                '--z',     '1.41',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  '0.0',

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_right_a'
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='center1_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '0.75',
                '--y',     '0.0',
                '--z',     '1.91',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  '0.0',

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_center_a'
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='center2_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '0.75',
                '--y',     '0.0',
                '--z',     '1.91',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  str(math.pi),

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_center_a_laser_data_frame'
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='left2_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '0.75',
                '--y',     '0.5',
                '--z',     '1.3',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  str(math.pi),

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_left_a_laser_data_frame'
            ],
        ),  
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='right2_os_front_tf_publisher',
            output='screen',
            arguments=[
                '--x',     '1.53',
                '--y',     '-0.5',
                '--z',     '1.41',
                '--yaw',   '0.0',
                '--pitch', '0.0',
                '--roll',  str(math.pi),

                '--frame-id',       'base_link',
                '--child-frame-id', 'os_right_a_laser_data_frame'
            ],
        ),

    ])