#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (58.51%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    27.3K
# Total Submissions: 42.8K
# Testcase Example:  '"(abcd)"'
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 
# 注意，您的结果中 不应 包含任何括号。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "(abcd)"
# 输出："dcba"
# 
# 
# 示例 2：
# 
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 
# 
# 示例 3：
# 
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 
# 
# 示例 4：
# 
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
# 
# 
#

# @lc code=start
class Solution:
    s = ""
    def reverse(self, p: int):
        i = p+1
        q = p
        while i < len(self.s) and self.s[i] != ')':
            if self.s[i] == "(":
                self.reverse(i)
            else:
                i += 1
        q = i
        self.s = self.s[0:p] + self.s[q-1:p:-1] + self.s[q+1:]
    def reverseParentheses(self, s: str) -> str:
        self.s = s
        i = 0
        while True:
            if i >= len(self.s):
                break
            if self.s[i] == "(":
                self.reverse(i)
            else:
                i += 1
        return self.s
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    r = s.reverseParentheses("bokgr(wfh)()ab()vlpekccptczn((h)qgmtqakq)mxo()e(p)dpsuo()()jegpssbfh((i))vptzzgcnqu(bnn()tw)hmxucjtzxnl(az(p)a)e(u(j(sy(v)m(yat)h))uv(bhhu(ro)uf((p)pv)itddbp)f)(p(jt)xshct(dzxnocm)ke)ql()ayoy((w(s(v)pvw(rozu)(m(wltj(n((pl((osniz)bo)a(a)f)l)))gmwu(()ax(c))jx(pa()w((rem(h(yuwqslf((j()s()(sdz(((hg(mr(())))))))))))))))))"
)
    print(r)