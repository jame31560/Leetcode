#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ary = []
        for each in range(0, len(nums), 2):
            for i in range(nums[each]):
                ary.append(nums[each+1])
        return ary
# @lc code=end
