import rclpy
from rclpy.node import Node
from gpiozero import Button ,PWMLED
from std_msgs.msg import String,Int32
from time import sleep


class Buttontalk(Node):

    def __init__(self):
        super().__init__('button')
        
        
    def __init__(self):
        super().__init__('buttontalk')
        self.publisher_ = self.create_publisher(String, 'ButtonTopic', 10) #the node topic
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
   
    
def main(args=None):
    rclpy.init(args=args)

    buttontalk = Buttontalk()

    rclpy.spin(buttontalk)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    buttontalk.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()