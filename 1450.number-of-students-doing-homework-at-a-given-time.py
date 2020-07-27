#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(
            1 if not(
                startTime[i] > queryTime or endTime[i] < queryTime
            ) else 0 for i in range(len(startTime)))

# @lc code=end
