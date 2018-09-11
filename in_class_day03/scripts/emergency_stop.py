#!/usr/bin/env python
<<<<<<< HEAD
''' This is a script to teleop the neato robots
	Isaac Vandor, Comprobo Fall 18
'''
from __future__ import print_function, division

import rospy
import tty
import select
import sys
import termios

from geometry_msgs.msg import Twist, Vector3
from neato_node.msg import Bump
from sensor_msgs.msg import LaserScan

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
        w
   a         d
        s
CTRL-C to quit
Spacebar to stop
"""
# Creating key bindings for moving and turning
moveBindings = {
		'w': (1),
		's': (-1)
	       }

turnBindings = {
		'a': (1),
		'd': (-1),
	      }
stopKey = ''

# some fanciness from Paul for setting button press and screen focus


def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


if __name__ == "__main__":
    print("Im here")
    settings = termios.tcgetattr(sys.stdin)
    
    class EmergencyStop():
        def __init__(self):
            self.key = None  # Assign key to something (it doesnt really matter what)
            # Initialize ROS publisher
            self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
            rospy.init_node('teleop_twist')  # Initialize ros node
            self.subBump = rospy.Subscriber('/bump',Bump, bump_Callback)
            self.subLaser = rospy.Subscriber('/stable_scan', LaserScan, laser_Callback)
            rospy.spin()
            move = rospy.get_param("~moving", .5)
            turn = rospy.get_param("~turn", 1.0)
            self.bumpData = Bump(0,0,0,0)
            self.laserData = None

            def bump_Callback(self, msg):
                #Callback for bump sensors
                self.bumpData = msg

            def laser_Callback(self, msg):
                #callback for laser data
                self.laserData = msg.ranges

            def has_bumped(self):
                # Takes no args, returns boolean based on bump or not
                if self.bumpData.leftFront or self.bumpData.rightFront or self.bumpData.leftSide or self.bumpData.rightSide:
                    return True
                return False

            def detect_obstacle(self):
                # Takes no args, returns boolean based on object
                for data in self.laserData:
                    if 0 < data < 0.5:
                        return True
                    return False
                    
            def runRobot(self):
                while self.key != '\x03':  # some fanciness from Paul to use Ctrl-C
                    key = getKey()
                    if key in moveBindings.keys():
                        move = moveBindings[key]
                    elif key in turnBindings.keys():
                        turn = turnBindings[key]
                    else:
                        move = 0
                        turn = 0

                    twist = Twist(linear=Vector3(y=0,z=0), angular=Vector3(x=0,y=0)) 
                    twist.linear.x = move 
                    twist.angular.z = turn

                    if key == stopKey:
                        twist.linear.x = 0
                        twist.angular.z = 0
                    elif self.has_bumped():
                            self.state = self.pub.publish(Twist(Vector3(-0.15,0,0),Vector3(0,0,0)))
                    elif self.detect_obstacle():
                            self.pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0.25)))
                    else:
                        self.pub.publish(twist) #run these jewels fast
            
=======

"""
Created on 29 July 2012
@author: Lisa Simpson
"""

from __future__ import print_function, division
import rospy
from neato_node.msg import Bump
from geometry_msgs.msg import Twist, Vector3

class EmergencyStopNode(object):
    def __init__(self):
        rospy.init_node('emergency_stop')
        rospy.Subscriber('/bump', Bump, self.process_bump)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.desired_velocity = 0.3

    def process_bump(self, msg):
        if any((msg.leftFront, msg.leftSide, msg.rightFront, msg.rightSide)):
            self.desired_velocity = 0.0

    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(Twist(linear=Vector3(x=self.desired_velocity)))
            r.sleep()

if __name__ == '__main__':
    estop = EmergencyStopNode()
    estop.run()
>>>>>>> 2046111ffbf66c217ec99bc57444c898be0c5d8a
