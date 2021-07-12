import rospy
from control_msgs.msg import JointTrajectoryControllerState
from sensor_msgs.msg import JointState

class SrMockHand():
    def __init__(self, hand_type, hand_id="rh"):
        self.pub_trajectory = rospy.Publisher("/"+hand_id+"_trajectory_controller/state", 
                                              JointTrajectoryControllerState, queue_size=1)
        self.pub_joint_state = rospy.Publisher("/joint_states", JointState, queue_size=1)