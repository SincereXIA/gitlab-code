#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#
# https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/description/
#
# algorithms
# Hard (47.88%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 14.8K
# Testcase Example:  '[1,2,3,5]\n3'
#
# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
# 
# 对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
# 
# 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] ==
# arr[j] 。
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,2,3,5], k = 3
# 输出：[2,5]
# 解释：已构造好的分数,排序后如下所示: 
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
# 很明显第三个最小的分数是 2/5
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,7], k = 1
# 输出：[1,7]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# 1 
# arr[0] == 1
# arr[i] 是一个 素数 ，i > 0
# arr 中的所有数字 互不相同 ，且按 严格递增 排序
# 1 
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left = 0.0
        right = 1.0
        while True:
            mid = (left + right) / 2
            count = 0
            max_val = 0
            max_pair = None
            for j in range(len(arr)):
                i = 0
                while arr[i] / arr[j] < mid:
                    if arr[i] / arr[j] > max_val:
                        max_val = arr[i] / arr[j]
                        max_pair = [arr[i], arr[j]]
                    count += 1
                    i += 1
                    if count > k:
                        break

            if count > k:
                right = mid
            elif count < k:
                left = mid
            else:
                return max_pair

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.kthSmallestPrimeFraction([1,2,3,5], 3)
    rs = s.kthSmallestPrimeFraction([1, 7], 1)
    print(rs)