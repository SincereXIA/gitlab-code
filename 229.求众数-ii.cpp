/*
 * @lc app=leetcode.cn id=229 lang=cpp
 *
 * [229] 求众数 II
 *
 * https://leetcode-cn.com/problems/majority-element-ii/description/
 *
 * algorithms
 * Medium (46.49%)
 * Likes:    448
 * Dislikes: 0
 * Total Accepted:    46.4K
 * Total Submissions: 93.5K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：[3,2,3]
 * 输出：[3]
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1]
 * 输出：[1]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：[1,1,1,3,3,2,2,2]
 * 输出：[1,2]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 5 * 10^4
 * -10^9 <= nums[i] <= 10^9
 * 
 * 
 * 
 * 
 * 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
 * 
 */
#include <vector>
#include <map>
#include <set>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        set<int> result;
        map<int, int> m;
        int threshold = nums.size()/3;
        for (auto n: nums) {
            auto i = m.find(n);
            if (i == m.end()) {
                m.insert(pair<int, int>(n, 1));
                if (1 >= threshold) {
                    result.insert(n);
                } 
                continue;
            }
            (*i).second += 1;
            if (i->second >= threshold) {
                result.insert(i->first);
            }
        }
        return vector<int>(result.begin(), result.end());
    }
};
// @lc code=end

