#!/usr/bin/env python
#
# Copyright 2019 Shadow Robot Company Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import rospy
import rospkg
from sr_run_trajectories.run_trajectories import SrRunTrajectories

if __name__ == "__main__":
    rospy.init_node('run_hand_poses')
    trajectories_file_path = rospkg.RosPack().get_path('sr_pose_tests') + '/config/hand_poses_to_test.yaml'
    srt = SrRunTrajectories(trajectories_file_path, arm=False)
    for pose in srt._hand_trajectories:
	if 'open' == pose:
	    continue
        raw_input("About to go to pose {}. Press [RETURN] to execute...".format(pose))
        srt.run_trajectory('hand', pose)
        raw_input("Press [RETURN] to go back to open pose")
        srt.run_trajectory('hand', 'open')
    rospy.loginfo("All poses have been tested. Exiting.")
