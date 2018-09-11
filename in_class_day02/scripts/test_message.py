#!/usr/bin/env python
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy

'''
class TestMessageNode(object):
    this node publishes a message at 2Hz
    def __init__(self):
        rospy.init_node('test_message')
        self.pub = rospy.Publisher('/my_point', PointStamped, queue_size=10)
    def run(self):
        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            my_point_stamped.header.stamp = rospy.Time.now()    # update timestamp
            publisher.publish(my_point_stamped)
            r.sleep()      

if __name__ == "__main__":
    my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
    my_point = Point(1.0, 2.0, 0.0)
    my_point_stamped = PointStamped(header=my_header, point=my_point)

    print my_point_stamped

'''
rospy.init_node('test_message')    # initialize ourselves with roscore
my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
my_point = Point(1.0, 2.0, 0.0)
my_point_stamped = PointStamped(header=my_header, point=my_point)

print my_point_stamped

publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
r = rospy.Rate(2)
while not rospy.is_shutdown():
    my_point_stamped.header.stamp = rospy.Time.now()    # update timestamp
    publisher.publish(my_point_stamped)
    r.sleep()