#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        check = []
        result = ""
        for each in S:
            if each == "(":
                result += each if check else ""
                check.append(each)
            elif each == ")":
                result += each if len(check) > 1 else ""
                check.pop(-1)
        return result

# @lc code=end
