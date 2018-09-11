#!/usr/bin/env python
""" Investigate receiving a message using a callback function """
from geometry_msgs.msg import PointStamped
import rospy

'''
class = ReceiveMessageNode(object):
    def __init__(self):
        rospy.init_node('receive_message')

'''
rospy.init_node('receive_message')

def process_point(msg):
    print msg.header

rospy.Subscriber("/my_point", PointStamped, process_point)

rospy.spin()