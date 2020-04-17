#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for each in str(n):
            sum += int(each)
            product *= int(each)
        return product-sum
# @lc code=end
