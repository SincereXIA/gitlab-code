#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (30.44%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    46.3K
# Total Submissions: 137.8K
# Testcase Example:  '"ab"\n"ba"'
#
# 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
# 
# 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
# 
# 
# 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ab", goal = "ba"
# 输出：true
# 解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。
# 
# 示例 2：
# 
# 
# 输入：s = "ab", goal = "ab"
# 输出：false
# 解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。
# 
# 示例 3：
# 
# 
# 输入：s = "aa", goal = "aa"
# 输出：true
# 解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。
# 
# 
# 示例 4：
# 
# 
# 输入：s = "aaaaaaabc", goal = "aaaaaaacb"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length, goal.length <= 2 * 10^4
# s 和 goal 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff_pair = None
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return False
        is_changed = False
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue
            if is_changed:
                return False
            if diff_pair == None:
                diff_pair = (s[i], goal[i])
            elif s[i] == diff_pair[1] and goal[i] == diff_pair[0]:
                is_changed = True
            else:
                return False
        if is_changed == False:
            if diff_pair:
                return False
            alphabet = set()
            for c in s:
                if c in alphabet:
                    return True
                alphabet.add(c)
            return False
        return True

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.buddyStrings("ab", "ba")