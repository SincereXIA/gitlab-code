#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode-cn.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (46.03%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 31.5K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 *
# ，返回所有能够得到目标值的表达式。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
# 
# 
# 示例 2:
# 
# 
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 
# 示例 3:
# 
# 
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
# 
# 示例 4:
# 
# 
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
# 
# 
# 示例 5:
# 
# 
# 输入: num = "3456237490", target = 9191
# 输出: []
# 
# 
# 
# 提示：
# 
# 
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        length = len(num)
        rs = []

        def deepSearch(p, op, before, history):
            old = history
            if op == '+':
                history = history + "+" + before + num[p]
            elif op == '-':
                history = history + "-" + before + num[p]
            elif op == '*':
                history = history + "*" + before + num[p]
            
            if p == length - 1:
                cmd = ""
                for i in range(len(history)):
                    if history[i] != '0' or i == len(history)-1:
                        cmd += history[i]
                    else:
                        if history[i+1] >= '0' and history[i+1] <= '9':
                            return
                        cmd += history[i]

                r = eval(cmd)
                if r == target:
                    rs.append(history[1:])
                return

            deepSearch(p+1, '+', '', history)
            deepSearch(p+1, '-', '', history)
            deepSearch(p+1, '*', '', history)

            deepSearch(p+1, op, before + num[p], old)
                    
        deepSearch(0, '+', '', '')
        return rs

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    r = s.addOperators("232", 8)
    print(r)
    r = s.addOperators("123", 6)
    print(r)
    r = s.addOperators("105", 5)
    print(r)
    r = s.addOperators("00", 0)
    print(r)
    r = s.addOperators("3456237490", 9191)
    print(r)

