#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (60.57%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    13K
# Total Submissions: 21.4K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,4]
# 输出：6
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [8,10,2]
# 输出：10
# 
# 
# 示例 5：
# 
# 
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        MAX_BIT_LEN = 32
        for k in range(MAX_BIT_LEN, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)
            
            next_x = x*2 + 1
            find = False
            for num in nums:
                if next_x ^ (num >> k) in seen:
                    find = True
                    break
            if find:
                x = next_x
            else:
                x = next_x -1
        return x

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
