#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (47.87%)
# Likes:    776
# Dislikes: 0
# Total Accepted:    179.9K
# Total Submissions: 372K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
#  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# 输出：true
#
#
# 示例 2：
#
#
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# 输出：false
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9 <= target <= 10^9
#
#
#
from typing import *
# @lc code=start

class Node:
    next = None
    value = 0
    def __init__(self, value):
        self.value = value


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        y = 0
        x = 0
        while y < n and y < m:
            if matrix[y][y] < target:
                y += 1
            else:
                break
        if y >= n or y >= m:
          y -= 1
        x = y
        if matrix[y][y] < target:
            while y < n:
                if matrix[x][y] < target:
                    y += 1
                else:
                    break
            while x < m:
                if matrix[x][y] < target:
                    x += 1
                else:
                    break

        if matrix[x][y] == target:
            return True

        for c in range(y-1, -1, -1):
            if matrix[x][c] == target:
                return True
            elif matrix[x][c] < target:
                break

        for r in range(x-1, -1, -1):
            if matrix[r][y] == target:
                return True
            elif matrix[r][y] < target:
                break

        return False


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
        3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    rs = s.searchMatrix(matrix, 13)
    print(rs)
