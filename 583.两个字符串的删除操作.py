#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (58.77%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 66.4K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 
# 
# 示例：
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 
# 
# 提示：
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
# 
# 
#

# @lc code=start
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        p = 0
        q = 0 
        rs = 0
        while p < len(word1) and q < len(word2):
            if word1[p] != word2[q]:
                costp = 1
                for i in range(p+1, len(word1)):
                    if word1[i] == word2[q]:
                        break
                    costp += 1
                costq = 1
                for i in range(q+1, len(word2)):
                    if word1[p] == word2[i]:
                        break
                    costq += 1
                
                if p + costp == len(word1) and q + costq == len(word2):
                    rs += 2
                else:
                    if costp < costq:
                        p += costp
                        rs += costp
                    else:
                        q += costq
                        rs += costq
            if p < len(word1) and q < len(word2):
                p += 1
                q += 1
                
        p = len(word1) if p > len(word1) else p
        q = len(word2) if q > len(word2) else q
        return rs + len(word1) - p + len(word2) - q

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [ [0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        last = [ [(0, 0) for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for x in range(1, len(word1)+1):
            for y in range(1, len(word2)+1):
                r1 = dp[x-1][y]
                r2 = dp[x][y-1]
                if r1 > r2:
                    dp[x][y] = r1
                    last[x][y] = last[x-1][y]
                else:
                    dp[x][y] = r2
                    last[x][y] = last[x][y-1]
                if word2[y-1] == word1[x-1] and last[x-1][y][1] < y and last[x][y-1][0] < x:
                    dp[x][y] += 1
                    last[x][y] = (x,y)
        return len1 + len2 - 2 * dp[len1][len2]

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    rs = s.minDistance("intention","execution")
    print(rs)
