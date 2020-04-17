#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for each in nums:
            count = 0
            for i in nums:
                if i < each:
                    count += 1
            result.append(count)
        return result


# @lc code=end
