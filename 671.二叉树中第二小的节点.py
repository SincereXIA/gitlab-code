#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (47.80%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    42K
# Total Submissions: 87.9K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,2,5,null,null,5,7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,2,2]
# 输出：-1
# 解释：最小的值是 2, 但是不存在第二小的值。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 25] 内
# 1 
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)
# 
# 
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        def findMinBigger(val, root:TreeNode) -> int:
            if root.val > val:
                return root.val
            min_left = -1
            min_right = -1
            if root.left:
                min_left = findMinBigger(val, root.left)
            if root.right:
                min_right = findMinBigger(val, root.right)
            if min_left == -1:
                return min_right
            elif min_right == -1:
                return min_left
            else:
                return min(min_right, min_left)

        return findMinBigger(root.val, root)        

# @lc code=end

