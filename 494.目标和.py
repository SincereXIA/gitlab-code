#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (46.17%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    93.5K
# Total Submissions: 199K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 target 。
# 
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 
# 
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 
# 
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], target = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# -1000 
# 
# 
#
from typing import *
# @lc code=start
MAX_SUM = 1000
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [ [ 0 for _ in range(2*MAX_SUM+1)] for _ in range(len(nums))]
        first = nums[0]
        dp[0][MAX_SUM+first] += 1
        dp[0][MAX_SUM-first] += 1
        for k in range(1,len(nums)):
            num = nums[k]
            for t in range(2*MAX_SUM+1):
                if t-num < 0:
                    small = 0
                else:
                    small = dp[k-1][t-num]
                if t+num >= 2*MAX_SUM+1:
                    big = 0
                else:
                    big = dp[k-1][t+num]
                dp[k][t] = small + big
        return dp[len(nums)-1][MAX_SUM+target]


# @lc code=end

if __name__ == "__main__" :
    s = Solution()
    rs = s.findTargetSumWays([0,0,0,0,0,0,0,0,1], 3)
    print(rs)
