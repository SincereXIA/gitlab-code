#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (34.94%)
# Likes:    1218
# Dislikes: 0
# Total Accepted:    344.3K
# Total Submissions: 984.9K
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 
# 
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,1,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root, isLeft, father, min, max):

            if not root:
                return True
            
            if root.val <= min or root.val >= max:
                print(root.val)
                return False

            if isLeft:
                if root.val >= father:
                    print(root.val)
                    return False
            else:
                if root.val <= father:
                    return False
            nmax = max
            if root.val < max:
                nmax = root.val
            nmin = min
            if root.val > min:
                nmin = root.val
            return isValid(root.left, True, root.val, min, nmax) and isValid(root.right, False, root.val, nmin, max)
        
        min = -2**32
        max = 2**32
        return isValid(root.left, True, root.val, min, root.val) and isValid(root.right, False, root.val, root.val, max)
# @lc code=end

