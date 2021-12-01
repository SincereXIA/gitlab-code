#
# @lc app=leetcode.cn id=517 lang=python3
#
# [517] 超级洗衣机
#
# https://leetcode-cn.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (44.07%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 13K
# Testcase Example:  '[1,0,5]'
#
# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
# 
# 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
# 
# 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数
# 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：machines = [1,0,5]
# 输出：3
# 解释：
# 第一步:    1     0 <-- 5    =>    1     1     4
# 第二步:    1 <-- 1 <-- 4    =>    2     1     3    
# 第三步:    2     1 <-- 3    =>    2     2     2   
# 
# 
# 示例 2：
# 
# 
# 输入：machines = [0,3,0]
# 输出：2
# 解释：
# 第一步:    0 <-- 3     0    =>    1     2     0    
# 第二步:    1     2 --> 0    =>    1     1     1     
# 
# 
# 示例 3：
# 
# 
# 输入：machines = [0,2,0]
# 输出：-1
# 解释：
# 不可能让所有三个洗衣机同时剩下相同数量的衣物。
# 
# 
# 
# 
# 提示：
# 
# 
# n == machines.length
# 1 <= n <= 10^4
# 0 <= machines[i] <= 10^5
# 
# 
#
from typing import *
# @lc code=start
class Solution2:
    def findMinMoves(self, machines: List[int]) -> int:
        total = 0
        for m in machines:
            total += m
        average = total // len(machines)
        if total % len(machines) != 0:
            return -1
        move = True
        rs = 0
        while move:
            rs += 1
            move = False
            send = [ -1 for _ in machines ]
            print(machines)
            for i in range(len(machines)):
                if machines[i] >= average:
                    continue
                move = True
                for p in range(i-1, -1, -1):
                    if send[p] != -1:
                        break
                    if machines[p] > average:
                        machines[i] += 1
                        machines[p] -= 1
                        send[p] = i
                        break
            for i in range(len(machines)):
                if machines[i] >= average:
                    continue
                move = True
                for q in range(i+1, len(machines)):
                    if send[q] != -1:
                        break
                    if machines[q] > average:
                        machines[i] += 1
                        machines[q] -= 1
                        send[q] = i
                        break
        return rs - 1
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = 0
        for m in machines:
            total += m
        average = total // len(machines)
        if total % len(machines) != 0:
            return -1
        rs = 0
        need_operate = 0
        for m in machines:
            need_move = m - average # 有这么多衣服需要移走
            need_operate += need_move
            rs = max(rs, max(abs(need_operate), need_move))
        return rs

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.findMinMoves([0,0,10,0,0,0,10,0,0,0])
    print(rs)

