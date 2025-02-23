#!/usr/bin/env python3
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy


class MyNode(Node):

    def __init__(self):
        super().__init__('my_node')
        topic = "/chatter"
        self.get_logger().info('MyNode is listening to Topic -> ' + topic)
        self.sub = self.create_subscription(String, topic, self.chatter_callback, 5)
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.sub = self.create_subscription(String, topic, self.chatter_callback, qos_profile)

    def chatter_callback(self, msg: String):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()