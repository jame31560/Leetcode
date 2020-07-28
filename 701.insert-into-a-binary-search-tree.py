#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(tree, val):
            if tree:
                if val < tree.val:
                    tree.left = insert(tree.left, val)
                    return tree
                else:
                    tree.right = insert(tree.right, val)
                    return tree
            else:
                return TreeNode(val)
        return insert(root, val)
# @lc code=end
