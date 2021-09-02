#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (41.35%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 20.1K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
# 
# 子数组 是数组的一段连续部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,1,0,1], goal = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0,0,0], goal = 0
# 输出：15
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# nums[i] 不是 0 就是 1
# 0 
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {}
        sum = 0
        rs = 0
        for n in nums:
            sum += n
            want = sum - goal
            if want == 0:
                rs += 1
            if want in prefix.keys():
                rs += prefix[want]
            if sum in prefix.keys():
                prefix[sum] += 1
            else:
                prefix[sum] = 1
        return rs

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.numSubarraysWithSum([0,0,0,0,0], 0)
    print(rs)

