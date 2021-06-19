#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (41.25%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 41.2K
# Testcase Example:  '["un","iq","ue"]'
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
# 
# 请返回所有可行解 s 中最长长度。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
# 
# 
# 示例 2：
# 
# 输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
# 
# 
# 示例 3：
# 
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for pstr in arr:
            mask = 0
            for c in pstr:
                idx = ord(c) - ord("a")
                if (mask >> idx) & 1 :
                    mask = 0
                    break
                else:
                    mask |= 1 << idx
            if mask != 0:
                masks.append(mask)
        
        def ds(bits, p):
            if p >= len(masks):
                return bits

            mask = masks[p]
            if mask & bits != 0:
                return ds(bits, p+1)
            a = ds(bits | mask, p+1)
            b = ds(bits, p+1)
            if bin(a).count('1') > bin(b).count('1'):
                return a
            else:
                return b

        for m in masks:
            print(bin(m))

        rs = ds(0,0)
        return bin(rs).count('1')

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"])
    print(rs)
