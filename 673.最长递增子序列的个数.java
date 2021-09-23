/*
 * @lc app=leetcode.cn id=673 lang=java
 *
 * [673] 最长递增子序列的个数
 *
 * https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (39.25%)
 * Likes:    400
 * Dislikes: 0
 * Total Accepted:    32.2K
 * Total Submissions: 80.2K
 * Testcase Example:  '[1,3,5,4,7]'
 *
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [1,3,5,4,7]
 * 输出: 2
 * 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [2,2,2,2,2]
 * 输出: 5
 * 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 * 
 * 
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 * 
 */

// @lc code=start
class Solution673 {
    public int findNumberOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int[] cnt = new int[nums.length]; // 最长数组个数
        dp[0] = 1;
        cnt[0] = 1;
        for (int i = 1; i < nums.length; i++){
            int num = nums[i];
            int max = dp[i-1]; // 当前最常递增子序列长度
            dp[i] = 1;
            cnt[i] = 1; // 
            for (int j = 0; j < i; j++) {
                int c = 0;
                if (num > nums[j]) {
                    c = dp[j] + 1;
                }
                if (c > max) {
                    max = c;
                    cnt[i] = cnt[j];
                } else if (c == max) {
                    cnt[i] += cnt[j];
                }
            }
            dp[i] = max;
        }
        return cnt[nums.length-1];
    }
}
// @lc code=end
class Main {
    public static void main(String[] args) {
        Solution673 s = new Solution673();
        int[] input = {1,2,4,3,5,4,7,2};
        int rs = s.findNumberOfLIS(input);
        System.out.println(rs);
    }
}