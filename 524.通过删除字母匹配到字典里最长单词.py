#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (47.32%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    60.9K
# Total Submissions: 124.4K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# s 和 dictionary[i] 仅由小写英文字母组成
# 
# 
#
from typing import *
# @lc code=start

def sf(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b) :
        return False
    else:
        return a < b


class Solution:
    def isin(self, key, word):
        p = 0
        q = 0
        while p < len(word):
            if key[q] == word[p] :
                p += 1
                q += 1
                if q >= len(key):
                    return True
            else:
                p += 1
        return False

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        sd = sorted(dictionary, key=lambda x: (-len(x), x), reverse=False)
        print(sd)
        for k in sd:
            if self.isin(k, s):
                return k
        return ""
# @lc code=end
if __name__ == "__main__" :
    s = Solution()
    rs = s.findLongestWord("abce", ["abe", "abc"])
    print(rs)
