#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#
# https://leetcode-cn.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (50.08%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 44K
# Testcase Example:  '[1,2]\n3'
#
# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
# 
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
# 
# 
# 
# 示例 1：
# 
# 输入：people = [1,2], limit = 3
# 输出：1
# 解释：1 艘船载 (1, 2)
# 
# 
# 示例 2：
# 
# 输入：people = [3,2,2,1], limit = 3
# 输出：3
# 解释：3 艘船分别载 (1, 2), (2) 和 (3)
# 
# 
# 示例 3：
# 
# 输入：people = [3,5,3,4], limit = 5
# 输出：4
# 解释：4 艘船分别载 (3), (3), (4), (5)
# 
# 提示：
# 
# 
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000
# 
# 
#

from typing import *
# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        p = 0
        q = len(people) - 1
        rs = 0
        while p <= q:
            if p == q:
                rs += 1
                break
            if people[p] + people[q] <= limit:
                rs += 1
                p += 1
                q -= 1
            else:
                rs += 1
                q -= 1
        return rs
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.numRescueBoats([3,5,3,4], 5)
    print(rs)
