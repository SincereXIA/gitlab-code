#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (48.39%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    51.3K
# Total Submissions: 102.7K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 'A'、'C'、'G' 或 'T'
# 
# 
#
from typing import *
from collections import defaultdict
# @lc code=start

TO_BIN = {'A': 0, 'T': 1, 'C': 2, 'G': 3}

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        wind = s[i:i+9]
        wind_bin = 0
        for w in wind:
            wind_bin = (wind_bin << 2) | TO_BIN[w]
        count = defaultdict(int)
        i = 9
        rs = []
        while i < len(s):
            w = s[i]
            wind_bin = ((wind_bin << 2) | TO_BIN[w]) & ( (1 << 20) - 1 )
            i += 1
            count[wind_bin] += 1
            if count[wind_bin] == 2:
                rs.append(s[i-10:i])
        return rs



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.findRepeatedDnaSequences("AAAAAAAAAAAAA")
    print(rs)
