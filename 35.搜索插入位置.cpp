/*
 * @lc app=leetcode.cn id=35 lang=cpp
 *
 * [35] 搜索插入位置
 *
 * https://leetcode-cn.com/problems/search-insert-position/description/
 *
 * algorithms
 * Easy (47.02%)
 * Likes:    929
 * Dislikes: 0
 * Total Accepted:    389.4K
 * Total Submissions: 828.2K
 * Testcase Example:  '[1,3,5,6]\n5'
 *
 * 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
 * 
 * 你可以假设数组中无重复元素。
 * 
 * 示例 1:
 * 
 * 输入: [1,3,5,6], 5
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1,3,5,6], 2
 * 输出: 1
 * 
 * 
 * 示例 3:
 * 
 * 输入: [1,3,5,6], 7
 * 输出: 4
 * 
 * 
 * 示例 4:
 * 
 * 输入: [1,3,5,6], 0
 * 输出: 0
 * 
 * 
 */
#include <iostream>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i<nums.size(); i++) {
            cout << i << ": " << nums[i] <<  endl;
            if (target <= nums[i]) {
                return i;
            }
        }
        return nums.size();
    }
};
// @lc code=end

int main(int argc, const char** argv) {
    int n[] = {1,3,5,6};
    vector<int> nums(n, n+4);
    Solution s = Solution();
    int rs = s.searchInsert(nums, 7);
    std::cout << rs << std::endl;
    return 0;
}
