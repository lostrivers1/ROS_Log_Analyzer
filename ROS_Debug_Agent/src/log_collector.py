# 订阅 ROS 日志节点，保存日志
import rospy
from rosgraph_msgs.msg import Log

def callback(msg):
    with open("logs.txt", "a") as f:
        f.write(f"{msg.header.stamp}: {msg.msg}\n")

rospy.init_node("log_collector")
rospy.Subscriber('/rosout', Log, callback)
rospy.spin()
