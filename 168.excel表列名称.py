#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (39.44%)
# Likes:    405
# Dislikes: 0
# Total Accepted:    66.1K
# Total Submissions: 157.9K
# Testcase Example:  '1'
#
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# 
# 例如：
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：columnNumber = 1
# 输出："A"
# 
# 
# 示例 2：
# 
# 
# 输入：columnNumber = 28
# 输出："AB"
# 
# 
# 示例 3：
# 
# 
# 输入：columnNumber = 701
# 输出："ZY"
# 
# 
# 示例 4：
# 
# 
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber = int(columnNumber)
        #n为待转换的十进制数，x为机制，取值为2-16
        b=[]
        while True:
            s=(columnNumber-1)//26  # 商
            y=(columnNumber-1)%26  # 余数
            b.append(y)
            if s==0:
                break
            columnNumber=s
        b.reverse()
        rs = ""
        for i in b:
            rs += chr(ord('A')+i)
        return rs
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.convertToTitle("701")
    print(rs)