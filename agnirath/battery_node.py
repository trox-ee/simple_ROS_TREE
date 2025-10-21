#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray as temp_array
from std_msgs.msg import Float32

class Subscriber_node(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.subscriber_ = self.create_subscription(
            Float32, '/battery_temp_pub', self.callback, 1)
        
    def callback(self, battery_temp):
        self.get_logger().info("Battery state - (" + str(battery_temp.data) + ")")


def main(args = None):
    rclpy.init(args=args)
    node = Subscriber_node()
    rclpy.spin(node)
    rclpy.node.destroy_node()
    rclpy.shutdown()