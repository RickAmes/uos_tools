#!/usr/bin/env python
import roslib; roslib.load_manifest('acc_finder')
import rospy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

lin_min = 0.0
lin_max = 0.0
ang_min = 0.0
ang_max = 0.0

def odom_cb(msg):
    global lin_min, lin_max, ang_min, ang_max
    if lin_min > msg.twist.twist.linear.x:
        lin_min = msg.twist.twist.linear.x
    if lin_max < msg.twist.twist.linear.x:
        lin_max = msg.twist.twist.linear.x
    if ang_min > msg.twist.twist.angular.z:
        ang_min = msg.twist.twist.angular.z
    if ang_max < msg.twist.twist.angular.z:
        ang_max = msg.twist.twist.angular.z

    rospy.loginfo('linear: [%f, %f]   angular: [%f, %f]', lin_min, lin_max,
            ang_min, ang_max)

def listener():
    rospy.init_node('acc_finder', anonymous=True)
    rospy.Subscriber('odom', Odometry, odom_cb)
    rospy.spin()

if __name__ == '__main__':
    listener()
