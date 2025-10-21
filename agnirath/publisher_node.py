#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32MultiArray as rosarray


class AnglePublisher(Node):
    def __init__(self):
        super().__init__('angle_publisher')
        
        # Create a publisher for topic 'publisher_data'
        self.publisher_ = self.create_publisher(
            rosarray, 'publisher_data', 1
            )

        # Set timer to call callback every second
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Create and publish a random array of two float values
        msg = rosarray()
        msg.data = [random.uniform(0.0, 100.0) for _ in range(2)]
        self.publisher_.publish(msg)

        # Log the data
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    angle_publisher = AnglePublisher()
    rclpy.spin(angle_publisher)
    angle_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
