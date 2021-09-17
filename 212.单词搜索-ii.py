#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (45.08%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    43.6K
# Total Submissions: 95.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
'["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1
# board[i][j] 是一个小写英文字母
# 1
# 1
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
#
#
#
from typing import *
# @lc code=start
from collections import defaultdict

class Tire:
    def __init__(self):
        self.children = defaultdict(Tire)
        self.word = ""
    def insert(self, word: str):
        t = self
        for c in word:
            t = t.children[c]
        t.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire = Tire()
        for word in words:
            tire.insert(word)

        rs = set()
        
        def dfs(tire, x, y):
            if board[x][y] == "#":
                return
            c = board[x][y]
            board[x][y] = "#"
            if tire.children[c].word != "":
                rs.add(tire.children[c].word)
                return
            move = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            for m in move:
                if 0 <= m[0] < len(board) and 0 <= m[1] < len(board[0]):
                    dfs(tire.children[c], m[0], m[1])
            board[x][y] = c

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(tire, i, j)

        return list(rs)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    rs = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
    print(rs)