#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is not None:
            if root.val >= L and root.val <= R:
                return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
            else:
                return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        else:
            return 0


# @lc code=end
