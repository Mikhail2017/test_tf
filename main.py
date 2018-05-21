#!/usr/bin/env python
import rospy
import tf
import tf2_ros
import geometry_msgs.msg
import math
import numpy as np

rospy.init_node('tf2_turtle_broadcaster')

br = tf2_ros.StaticTransformBroadcaster()
t = geometry_msgs.msg.TransformStamped()
t.header.stamp = rospy.Time.now()
t.header.frame_id = "world"
t.child_frame_id = "camera"
t.transform.translation.x = 2.0
t.transform.translation.y = 0.
t.transform.translation.z = 1.0
#q = tf.transformations.quaternion_from_euler(math.pi/2, math.pi/2, 0)
m = np.array([[0, 0, 1, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
q = tf.transformations.quaternion_from_matrix(m)
t.transform.rotation.x = q[0]
t.transform.rotation.y = q[1]
t.transform.rotation.z = q[2]
t.transform.rotation.w = q[3]

br.sendTransform(t)

rospy.spin()