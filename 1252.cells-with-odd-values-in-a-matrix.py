#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ary = [[False for j in range(m)] for i in range(n)]
        for each in indices:
            row = each[0]
            col = each[1]
            ary[row] = [(not i) for i in ary[row]]
            for j in range(n):
                ary[j][col] = not ary[j][col]
        result = 0
        for each in ary:
            result += sum(1 if x else 0 for x in each)
        return result

# @lc code=end
