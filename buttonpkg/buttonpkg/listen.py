import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from gpiozero import PWMLED, Button #to install the gpiozero library if dont have it here the need here the linkk:https://gpiozero.readthedocs.io/en/latest/installing.html
from geometry_msgs.msg import Twist
led = PWMLED(4) #led is gpio4
b1 = Button(3) #b1 button  is gpio3
#this get activated blink get activated in the button subclass
def blink():
    if b1.is_pressed:
        led.off() 
        print("on")
    else:
        led.on()
        print("on")
      

class Buttonsub(Node):

    def __init__(self):
        super().__init__('buttonsub')
        self.subscription = self.create_subscription(
                        String,
            'ButtonTopic', #the node topic
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
       
   


     
    
    
    def listener_callback(self, msg,m1):
        blink()
      
      
      
        self.get_logger().info('the button works: "%s"' % msg.data)
    
    

       
  
     


def main(args=None):
   
    
    rclpy.init(args=args)

    buttonsub = Buttonsub()

    rclpy.spin(buttonsub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    buttonsub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
  