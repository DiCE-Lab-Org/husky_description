#!/usr/bin/env python3
"""
Launch RViz with the Husky A200-0876 description.

Usage:
    ros2 launch husky_description view_robot.launch.py
    ros2 launch husky_description view_robot.launch.py use_ros2_control:=false
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg_share = FindPackageShare("husky_description")

    # ---------------- Launch arguments ----------------
    declared_args = [
        DeclareLaunchArgument(
            "use_gazebo",
            default_value="false",
            description="Include Gazebo sensor plugins in the URDF.",
        ),
        DeclareLaunchArgument(
            "use_ros2_control",
            default_value="false",
            description="Include the ros2_control tag (disable for pure visualization).",
        ),
        DeclareLaunchArgument(
            "use_jsp_gui",
            default_value="true",
            description="Run joint_state_publisher_gui for interactive joint sliders.",
        ),
        DeclareLaunchArgument(
            "rviz_config",
            default_value=PathJoinSubstitution([pkg_share, "rviz", "view_robot.rviz"]),
            description="Path to the RViz configuration file.",
        ),
    ]

    use_gazebo        = LaunchConfiguration("use_gazebo")
    use_ros2_control  = LaunchConfiguration("use_ros2_control")
    use_jsp_gui       = LaunchConfiguration("use_jsp_gui")
    rviz_config       = LaunchConfiguration("rviz_config")

    # ---------------- Build URDF from xacro ----------------
    xacro_file = PathJoinSubstitution([pkg_share, "urdf", "robot.urdf.xacro"])
    robot_description_content = Command(
        [
            FindExecutable(name="xacro"), " ",
            xacro_file, " ",
            "use_gazebo:=",       use_gazebo,       " ",
            "use_ros2_control:=", use_ros2_control,
        ]
    )
    robot_description = {"robot_description": ParameterValue(robot_description_content, value_type=str)}

    # ---------------- Nodes ----------------
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    # Plain JSP (non-GUI) — used when use_jsp_gui is false
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        condition=_unless(use_jsp_gui),
    )

    # GUI JSP — used when use_jsp_gui is true
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        condition=_if(use_jsp_gui),
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
    )

    return LaunchDescription(
        declared_args
        + [robot_state_publisher, joint_state_publisher, joint_state_publisher_gui, rviz]
    )


# Small helpers so the conditions are readable above.
def _if(expr):
    from launch.conditions import IfCondition
    return IfCondition(expr)


def _unless(expr):
    from launch.conditions import UnlessCondition
    return UnlessCondition(expr)
