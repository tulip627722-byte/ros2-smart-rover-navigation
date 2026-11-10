#!/usr/bin/env python3
"""Save map from /map topic with correct QoS."""
import sys
import os
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, HistoryPolicy
from nav_msgs.msg import OccupancyGrid
import struct
import zlib


class MapSaver(Node):
    def __init__(self):
        super().__init__('map_saver_simple')
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, qos)
        self.map_received = False
        self.get_logger().info('Waiting for map on /map topic (timeout: 15s)...')

    def save_pgm(self, map_msg, filepath):
        """Save OccupancyGrid as PGM + YAML."""
        w, h = map_msg.info.width, map_msg.info.height
        # Convert occupancy grid to PGM (0=free=white, 100=occupied=black)
        pgm_data = bytearray()
        for cell in map_msg.data:
            if cell == -1:  # Unknown
                pix = 205  # gray
            elif cell == 0:  # Free
                pix = 254
            elif cell >= 100:  # Occupied
                pix = 0
            else:
                pix = int((100 - cell) * 254 / 100)
            pgm_data.extend(struct.pack('B', pix))

        # Write PGM
        pgm_path = filepath + '.pgm'
        with open(pgm_path, 'wb') as f:
            f.write(f'P5\n# CREATOR: map_saver_simple\n{w} {h}\n255\n'.encode())
            f.write(bytes(pgm_data))
        self.get_logger().info(f'Saved {pgm_path} ({w}x{h})')

        # Write YAML
        yaml_path = filepath + '.yaml'
        yaml_content = f"""image: {os.path.basename(pgm_path)}
resolution: {map_msg.info.resolution}
origin: [{map_msg.info.origin.position.x}, {map_msg.info.origin.position.y}, 0.0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.25
"""
        with open(yaml_path, 'w') as f:
            f.write(yaml_content)
        self.get_logger().info(f'Saved {yaml_path}')

    def map_callback(self, msg):
        if self.map_received:
            return
        self.map_received = True
        self.get_logger().info('Map received! Saving...')
        filepath = sys.argv[1] if len(sys.argv) > 1 else '/tmp/map'
        self.save_pgm(msg, filepath.replace('.pgm', '').replace('.yaml', ''))
        self.get_logger().info('Map saved successfully!')
        # Shutdown after saving
        raise SystemExit(0)


def main(args=None):
    rclpy.init(args=args)
    node = MapSaver()
    timer = node.create_timer(15.0, lambda: setattr(node, '_timeout', node.destroy_node() or setattr(rclpy, '_shutdown', rclpy.shutdown()) or exec('raise SystemExit(0)')))
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
