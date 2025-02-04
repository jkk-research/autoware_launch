# Copyright 2023 Ouster, Inc.
#

"""Launch a sensor node along with..."""

from pathlib import Path
import launch
import lifecycle_msgs.msg
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node, LifecycleNode
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            RegisterEventHandler, EmitEvent, LogInfo)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.events import matches_action
from launch_ros.events.lifecycle import ChangeState
from launch_ros.event_handlers import OnStateTransition
#from launch_ros.actions import SetRemap
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    """
    Generate launch description for running ouster_ros components separately each
    component will run in a separate process).
    """
    aw_pkg_dir = get_package_share_directory('autoware_launch')
    default_params_file = \
        Path(aw_pkg_dir) / 'launch' / 'lidar_config.yaml'
    params_file = LaunchConfiguration('params_file')
    params_file_arg = DeclareLaunchArgument('params_file',
                                            default_value=str(
                                                default_params_file),
                                            description='name or path to the parameters file to use.')

    ouster_ns = LaunchConfiguration('ouster_ns')
    ouster_ns_arg = DeclareLaunchArgument('ouster_ns', default_value='lexus3/os_left')


    os_driver = LifecycleNode(
        package='ouster_ros',
        executable='os_driver',
        name="os_driver",
        namespace="",
        parameters=[params_file],
        output='screen',
    )


    # os_sensor = LifecycleNode(
    #     package='ouster_ros',
    #     executable='os_sensor',
    #     name='os_sensor',
    #     namespace='',
    #     parameters=[params_file],
    #     output='screen',
    # )

    sensor_configure_event = EmitEvent(
        event=ChangeState(
            lifecycle_node_matcher=matches_action(os_driver),
            transition_id=lifecycle_msgs.msg.Transition.TRANSITION_CONFIGURE,
        )
    )

    sensor_activate_event = RegisterEventHandler(
        OnStateTransition(
            target_lifecycle_node=os_driver, goal_state='inactive',
            entities=[
                LogInfo(msg="os_driver activating... lexus3/os_left"),
                EmitEvent(event=ChangeState(
                    lifecycle_node_matcher=matches_action(os_driver),
                    transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVATE,
                )),
            ],
            handle_once=True
        )
    )

    

    # TODO: figure out why registering for on_shutdown event causes an exception
    # and error handling
    # shutdown_event = RegisterEventHandler(
    #     OnShutdown(
    #         on_shutdown=[
    #             EmitEvent(event=ChangeState(
    #               lifecycle_node_matcher=matches_node_name(node_name=F"/ouster/os_sensor"),
    #               transition_id=lifecycle_msgs.msg.Transition.TRANSITION_ACTIVE_SHUTDOWN,
    #             )),
    #             LogInfo(msg="os_sensor node exiting..."),
    #         ],
    #     )
    # )

    # os_cloud = Node(
    #     package='ouster_ros',
    #     executable='os_cloud',
    #     name='os_cloud',
    #     namespace=ouster_ns,
    #     parameters=[params_file],
    #     output='screen',
    # )

    # os_image = Node(
    #     package='ouster_ros',
    #     executable='os_image',
    #     name='os_image',
    #     namespace=ouster_ns,
    #     parameters=[params_file],
    #     output='screen',
    # )
    
    # return launch.LaunchDescription([
    #     params_file_arg,
    #     ouster_ns_arg,
    #     os_sensor,
    #     os_cloud,
    #     # os_image,
    #     sensor_configure_event,
    #     sensor_activate_event,
    #     # shutdown_event
    # ])

    return launch.LaunchDescription([
        GroupAction(
            actions=[
                PushRosNamespace('lexus3/os_left'),
                params_file_arg,
                ouster_ns_arg,
                os_driver,
                # os_cloud,
                # os_image,
                sensor_configure_event,
                sensor_activate_event,
            ]
        )
    ])
