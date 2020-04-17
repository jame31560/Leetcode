#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L_count = 0
        R_count = 0
        result = 0
        for each in s:
            if each == "L":
                L_count += 1
            else:
                R_count += 1
            if L_count == R_count:
                L_count = 0
                R_count = 0
                result += 1
        return result

# @lc code=end
