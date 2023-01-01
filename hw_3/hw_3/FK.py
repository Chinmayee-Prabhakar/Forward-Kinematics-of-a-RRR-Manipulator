import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray

import math
import numpy as np

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'topic',
            self.listener_callback,
            1)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        q1=msg.data[0]
        q2=msg.data[1]
        q3=msg.data[2]
        l1=1 #assuming link length to be of 1 unit
        l2=1 #assuming link length to be of 1 unit
        l3=1 #assuming link length to be of 1 unit
        
        A1 = np.array([[math.cos(q1),0, (-math.sin(q1)),0],[math.sin(q1),0,math.cos(q1),0],[0,-1,0,l1],[0,0,0,1]])
        A2 = np.array([[math.cos(q2),(-math.sin(q2)),0,(l2*math.cos(q2))],[math.sin(q2),math.cos(q2),0,(l2*math.sin(q2))],[0,0,1,0],[0,0,0,1]])
        A3 = np.array([[math.cos(q3),(-math.sin(q3)),0,(l3*math.cos(q3))],[math.sin(q3),math.cos(q3),0,(l3*math.sin(q3))],[0,0,1,0],[0,0,0,1]])
        
        
        t = A1.dot(A2)
        T = t.dot(A3)

        print("The pose of the end-effector is:")
        print(T)

                     

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)


    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() 
    main() 
