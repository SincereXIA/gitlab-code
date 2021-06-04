#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (40.35%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 36.8K
# Testcase Example:  '[1,2,3]'
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
# 
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 
# 
# 如果存在多个有效解子集，返回其中任何一个均可。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# nums 中的所有整数 互不相同
# 
# 
#
from typing import *
# @lc code=start

        

class Solution:
    DP = []
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [1 for _ in nums]
        MAX = 1
        MAX_I = 0
        for i in range(1, len(nums)):
            maxSize = 1
            for j in range(0, i):
                if nums[i]%nums[j] == 0:
                    #print(f'{nums[i]} | {nums[j]}')
                    s = dp[j] + 1
                    if s > maxSize:
                        maxSize = s
            dp[i] = maxSize
            if dp[i] > MAX:
                MAX = dp[i]
                MAX_I = i
        print(dp)
        self.DP = dp
        return self.getResult(nums, MAX, nums[MAX_I])

    def getResult(self, nums: List[int], maxSize: int, next:int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            if self.DP[i] == maxSize and next%nums[i] == 0:
                #print(nums[i])
                rs = self.getResult(nums[0:i], maxSize-1, nums[i])
                rs.append(nums[i])
                return rs
        return []
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.largestDivisibleSubset([2,3,4,8]))
