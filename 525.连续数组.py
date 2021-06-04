#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
# https://leetcode-cn.com/problems/contiguous-array/description/
#
# algorithms
# Medium (45.28%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 31.6K
# Testcase Example:  '[0,1]'
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
# 
# 示例 2:
# 
# 
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
# 
# 
# 
# 提示：
# 
# 
# 1 
# nums[i] 不是 0 就是 1
# 
# 
#
from typing import *
# @lc code=start

class delta:
    def __init__(self, d, l):
        self.d = d
        self.l = l
    def __hash__(self):
        return hash(self.d)
    def __eq__(self, o):
        if not isinstance(o, delta):
            return False
        return self.d == o.d 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        deltaDict = {}
        num1 = 0
        num0 = 0
        maxL = 0
        deltaDict[0] = 0
        for num in nums:
            if num == 0:
                num0 += 1
            else:
                num1 += 1
            if num0 - num1 not in deltaDict.keys():
                deltaDict[num0-num1] = num0+num1
            if num0 - num1 in deltaDict.keys():
                l = deltaDict.get(num0 - num1)
                sameL = num1 + num0 - l
                if sameL > maxL:
                    maxL = sameL
        return maxL

            

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.findMaxLength([0,0,1,0,0,0,1,1])
    print(rs)

