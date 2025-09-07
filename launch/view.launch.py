# Import necessary modules
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	urdf_file = os.path.join(
		os.path.dirname(__file__), '..', 'urdf', 'ratze.urdf'
	)
	with open(urdf_file, 'r') as infp:
		robot_description = infp.read()

	return LaunchDescription([
		Node(
			package='joint_state_publisher_gui',
			executable='joint_state_publisher_gui',
			name='joint_state_publisher_gui',
		),
		Node(
			package='robot_state_publisher',
			executable='robot_state_publisher',
			name='robot_state_publisher',
			output='screen',
			parameters=[{'robot_description': robot_description}],
		),
		Node(
			package='rviz2',
			executable='rviz2',
			name='rviz2',
			output='screen',
		),
	])
