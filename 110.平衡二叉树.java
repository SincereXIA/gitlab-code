/*
 * @lc app=leetcode.cn id=110 lang=java
 *
 * [110] 平衡二叉树
 *
 * https://leetcode-cn.com/problems/balanced-binary-tree/description/
 *
 * algorithms
 * Easy (56.32%)
 * Likes:    768
 * Dislikes: 0
 * Total Accepted:    252.9K
 * Total Submissions: 449K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，判断它是否是高度平衡的二叉树。
 * 
 * 本题中，一棵高度平衡二叉树定义为：
 * 
 * 
 * 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：true
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：root = [1,2,2,3,3,null,null,4,4]
 * 输出：false
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：root = []
 * 输出：true
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中的节点数在范围 [0, 5000] 内
 * -10^4 
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int dl = 0;
        int dr = 0;
        dl = depth(root.left);
        dr = depth(root.right);
        return dl > dr ? dl + 1 : dr + 1; 
    }

    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        // if (root.left == null) {
        //     return depth(root.right) < 1;
        // }
        // if (root.right == null) {
        //     return depth(root.left) < 1;
        // }

        boolean bl = isBalanced(root.left);
        if (! bl) {
            return false;
        }
        boolean br = isBalanced(root.right);
        if (! br) {
            return false;
        }
        int dl = depth(root.left);
        int dr = depth(root.right);
        if (dl - dr > 1 || dl - dr < -1) {
            return false;
        }
        return true;
    }
}
// @lc code=end

