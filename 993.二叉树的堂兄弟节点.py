#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#
# https://leetcode-cn.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.10%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 69.3K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepSearch(self, root: TreeNode, x:int, deep: int, parent: int) -> (int, int):
        if root.val == x:
            return (deep, parent)
        if root.left:
            deep_left = self.deepSearch(root.left, x, deep+1, root.val)
            if deep_left != -1:
                return deep_left
        if root.right:
            deep_right = self.deepSearch(root.right, x, deep+1, root.val)
            if deep_right != -1:
                return deep_right
        return -1

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dx = self.deepSearch(root, x, 0, -1)
        dy = self.deepSearch(root, y, 0, -1)
        return dx[0] == dy[0] and dx[1]!=dy[1]
        
# @lc code=end

