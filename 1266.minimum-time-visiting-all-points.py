#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        now = points.pop(0)
        step = 0
        while(points != []):
            x_bar = abs(points[0][0]-now[0])
            y_bar = abs(points[0][1]-now[1])
            step += (min(x_bar, y_bar) + abs(x_bar-y_bar))
            now = points.pop(0)
        return step

# @lc code=end
