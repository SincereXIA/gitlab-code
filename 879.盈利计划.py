#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
# https://leetcode-cn.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (39.75%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 12.7K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
# 
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 
# 示例 2：
# 
# 
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 1 
# 1 
# profit.length == group.length
# 0 
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]):
        MOD = 10**9 + 7
        dp = [ [ [ 0 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(profit)+1)]
        # i: 选择做 前 i 个工作
        # j: 选择 j 名员工
        # k： 最小盈利数量
        dp[0][0][0] = 1
        for i in range(1, len(profit)+1):
            members = group[i-1]
            earn = profit[i-1]
            for j in range(0, n+1):
                for k in range(0, minProfit+1):
                    # print(i, j, k)
                    if j < members:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-members][max(0, k-earn)] % MOD
        rs = 0
        for j in range(0, n+1):
            rs += dp[len(profit)][j][minProfit]
        return rs % MOD


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.profitableSchemes(10, 5, [2,3,5], [6,7,8])
    print(rs)
