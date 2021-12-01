#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#
# https://leetcode-cn.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (55.13%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 33.3K
# Testcase Example:  '1'
#
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
# 
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：1
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：10
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：16
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：24
# 输出：false
# 
# 
# 示例 5：
# 
# 输入：46
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 
# 
#
from collections import defaultdict
# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = defaultdict(int)
        num = n
        l = len(str(n))
        while num:
            n = num % 10
            nums[n] += 1
            num = num // 10
        target = 1
        while len(str(target)) <= l:
            if len(str(target)) == l:
                num = target
                cnums = nums.copy()
                find = True
                while num:
                    n = num % 10
                    cnums[n] -= 1
                    if cnums[n] < 0:
                        find = False
                        break
                    num = num // 10
                if find:
                    return True
            target *= 2
        return False
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.reorderedPowerOf2(46)
    print(rs)
