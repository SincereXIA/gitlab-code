#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (22.71%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 164.6K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 
# 
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 
# 
# 如果存在，返回 true ；否则，返回 false 。
# 
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 
# 示例 2：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
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
# 1 
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        last = 0
        lastm = 0
        mod  = set()
        mod.add(0)
        for num in nums:
            last = last + num
            prefix.append(last)
            m = last % k
            if m in mod and lastm != m:
                return True
            else:
                mod.add(m)
                if lastm == m:
                    lastm = -1
                else:
                    lastm = m
        return False
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.checkSubarraySum([1,0,1,0,1], 4)
    print(rs)

