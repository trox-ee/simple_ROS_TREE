#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray as temp_array
from std_msgs.msg import Float32

class middle_man(Node):
    def __init__(self):
        super().__init__('middle_man_node')
        self.subscriber_ = self.create_subscription(
            temp_array, "/publisher_data", self.callback, 10)
        
        self.motor_publisher_ = self.create_publisher(
            Float32, "motor_temp_pub", 10
        )
        self.battery_publisher_ = self.create_publisher(
            Float32, "battery_temp_pub", 10
        )

    def callback(self, values):
        msg = values.data
        msg_motor = 0.0 if msg[1] < 40.0 else 1.0
        msg_battery = 0.0 if msg[0] < 40.0 else 1.0       

        out_motor = Float32()
        out_battery = Float32()

        out_battery.data = msg_battery
        out_motor.data = msg_motor
        
        self.motor_publisher_.publish(out_motor)
        self.battery_publisher_.publish(out_motor) 

        self.get_logger().info(f"Received: {msg} | Published: {out_battery.data}, {out_motor.data}")



def main(args = None):
    rclpy.init(args = args)
    node = middle_man()
    rclpy.spin(node)
    rclpy.node.destroy_node()
    rclpy.shutdown()