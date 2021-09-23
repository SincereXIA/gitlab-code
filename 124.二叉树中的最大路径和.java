import jdk.nashorn.api.tree.Tree;

/*
 * @lc app=leetcode.cn id=124 lang=java
 *
 * [124] 二叉树中的最大路径和
 *
 * https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
 *
 * algorithms
 * Hard (44.41%)
 * Likes:    1224
 * Dislikes: 0
 * Total Accepted:    156.7K
 * Total Submissions: 352.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
 * 节点，且不一定经过根节点。
 * 
 * 路径和 是路径中各节点值的总和。
 * 
 * 给你一个二叉树的根节点 root ，返回其 最大路径和 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：root = [1,2,3]
 * 输出：6
 * 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
 * 
 * 示例 2：
 * 
 * 
 * 输入：root = [-10,9,20,null,null,15,7]
 * 输出：42
 * 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点数目范围是 [1, 3 * 10^4]
 * -1000 
 * 
 * 
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
class Solution {
    Integer max  = null;
    public int pathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int maxL = pathSum(root.left);
        int maxR = pathSum(root.right);
        if (maxL < 0) {
            maxL = 0;
        }
        if (maxR < 0) {
            maxR = 0;
        }
        int sum = maxL + maxR + root.val;
        if (max == null || max < sum) {
            max = sum;
            // System.out.println(max);
        }
        return maxL > maxR ? maxL + root.val : maxR + root.val;
    }


    public int maxPathSum(TreeNode root) {
        // 左 + 根
        // 右 + 根
        // 左 + 根 + 右（end）
        max = null;
        int pathSum = pathSum(root);
        return max > pathSum ? max : pathSum;
    }
}
// @lc code=end

