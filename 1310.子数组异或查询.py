#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#
# https://leetcode-cn.com/problems/xor-queries-of-a-subarray/description/
#
# algorithms
# Medium (66.87%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 40.5K
# Testcase Example:  '[1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]'
#
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
# 
# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor
# arr[Ri]）作为本次查询的结果。
# 
# 并返回一个包含给定查询 queries 所有结果的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8] 
# 解释：
# 数组中元素的二进制表示形式是：
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# 查询的 XOR 值为：
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8
# 
# 
# 示例 2：
# 
# 输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# 输出：[8,0,4,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 10^9
# 1 <= queries.length <= 3 * 10^4
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] < arr.length
# 
# 
#

from typing import *
# @lc code=start

DP = [[]]
ARR = []
class Solution:
    def query(self, start, end):
        global DP
        global ARR
        if DP[start][end] != -1:
            return DP[start][end]
        else:
            rs = self.query(start, end-1) ^ ARR[end]
            DP[start][end] = rs
            return rs

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for i in range(0, len(arr)):
            xors.append(xors[i] ^ arr[i])
        rs = []
        for q in queries:
            rs.append(xors[q[0]] ^ xors[q[1]+1])
        return rs
        
        
    def FxorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        global DP
        global ARR
        DP = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        ARR = arr
        for i in range(len(arr)):
            DP[i][i] = arr[i]
        rs = []
        for q in queries:
            rs.append(self.query(q[0], q[1]))
        return rs

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
    print(rs)
