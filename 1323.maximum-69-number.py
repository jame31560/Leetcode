#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == "6":
                return int(s[:i] + "9" + s[i+1:])
        return int(s)
# @lc code=end
