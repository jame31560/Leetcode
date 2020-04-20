#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for i in range(len(words)):
            words[i] = ("").join([code[ord(j)-97] for j in words[i]])
        return len(set(words))

# @lc code=end
