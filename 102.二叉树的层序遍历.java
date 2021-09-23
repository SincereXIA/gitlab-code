/*
 * @lc app=leetcode.cn id=102 lang=java
 *
 * [102] 二叉树的层序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (64.19%)
 * Likes:    1023
 * Dislikes: 0
 * Total Accepted:    393.4K
 * Total Submissions: 613K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
 * 
 * 
 * 
 * 示例：
 * 二叉树：[3,9,20,null,null,15,7],
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 返回其层序遍历结果：
 * 
 * 
 * [
 * ⁠ [3],
 * ⁠ [9,20],
 * ⁠ [15,7]
 * ]
 * 
 * 
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

import jdk.nashorn.api.tree.Tree;

import java.util.LinkedList;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
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
    int pow(int level) {
        int rs = 1;
        for (int i = 0; i < level; i++) {
            rs = rs * 2;
        }
        return rs;
    }
    class Qnode {
        int level;
        TreeNode node;
        Qnode(int level, TreeNode node) {
            this.level = level;
            this.node = node;
        }
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<Qnode> queue = new LinkedList<Qnode>();
        queue.add(new Qnode(0, root));
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<Integer>());
        int level = 0;
        while(!queue.isEmpty()){
            Qnode qnode = queue.poll();
            if (qnode.level > level) {
                level += 1;
                result.add(new ArrayList<Integer>());
            }
            result.get(level).add(qnode.node.val);
            TreeNode node = qnode.node;
            if (node.left != null) {
                queue.add(new Qnode(level + 1, node.left));
            }
            if (node.right!= null) {
                queue.add(new Qnode(level + 1, node.right));
            }
        }
        return result;
    }
}
// @lc code=end

