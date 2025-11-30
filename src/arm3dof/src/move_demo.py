#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time

class ArmMover(Node):
    def __init__(self):
        super().__init__('arm_mover_node')

        self.pub_j1 = self.create_publisher(Float64, 'j1_position_cmd', 10)
        self.pub_j2 = self.create_publisher(Float64, 'j2_position_cmd', 10)
        self.pub_j3 = self.create_publisher(Float64, 'j3_position_cmd', 10)

        self.get_logger().info("Waiting for 2 seconds...")

    def send_pose(self, j1_val, j2_val, j3_val):
        msg = Float64()

        # Joint 1
        msg.data = float(j1_val)
        self.pub_j1.publish(msg)

        # Joint 2
        msg.data = float(j2_val)
        self.pub_j2.publish(msg)

        # Joint 3
        msg.data = float(j3_val)
        self.pub_j3.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ArmMover()

    try:
        time.sleep(2.0)

        node.send_pose(0.0, 0.0, 0.0)
        time.sleep(3.0)

        node.send_pose(1.0, -0.5, -0.5)
        time.sleep(3.0)

        node.send_pose(-1.0, 0.5, 0.5)
        time.sleep(3.0)

        node.send_pose(0.0, 0.0, 0.0)
        node.get_logger().info("Movement scenario completed.")
        time.sleep(1.0)

    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
