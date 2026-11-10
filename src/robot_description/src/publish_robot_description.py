#!/usr/bin/env python3
"""Publish robot_description to /robot_description topic for RViz."""
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy
from std_msgs.msg import String


class RobotDescriptionPublisher(Node):
    def __init__(self):
        super().__init__('robot_description_publisher')
        # Use TRANSIENT_LOCAL durability so late subscribers receive the message
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            depth=1
        )
        self.pub = self.create_publisher(String, 'robot_description', qos)
        self.declare_parameter('robot_description', '')
        desc = self.get_parameter('robot_description').value
        if desc:
            msg = String()
            msg.data = desc
            # Publish multiple times for late subscribers
            self._publish_count = 0
            self._timer = self.create_timer(0.5, lambda: self._publish_msg(msg))
            self.get_logger().info('Publishing robot_description to /robot_description topic')
        else:
            self.get_logger().error('No robot_description parameter found!')

    def _publish_msg(self, msg):
        self.pub.publish(msg)
        self._publish_count += 1
        if self._publish_count >= 5:
            self.get_logger().info('Finished publishing robot_description')
            raise SystemExit(0)


def main(args=None):
    rclpy.init(args=args)
    node = RobotDescriptionPublisher()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
