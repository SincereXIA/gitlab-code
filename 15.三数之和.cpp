/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (33.28%)
 * Likes:    3691
 * Dislikes: 0
 * Total Accepted:    624.9K
 * Total Submissions: 1.9M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
 * 且不重复的三元组。
 * 
 * 注意：答案中不可以包含重复的三元组。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [-1,0,1,2,-1,-4]
 * 输出：[[-1,-1,2],[-1,0,1]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = []
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [0]
 * 输出：[]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * -10^5 
 * 
 * 
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> rs;
        if (nums.size() < 3) {
            return rs;
        }
        sort(nums.begin(), nums.end());
        for (auto n : nums) {
            cout << n << ", ";
        }
        cout << endl;
        for (int i = 0; i < nums.size() - 2;)
        {
            int j = i + 1;
            int k = nums.size()-1;
            while (j < k)
            {
                cout << i << j << k << endl;
                if (nums[i] + nums[j] + nums[k] > 0)
                {
                    cout << "k-1" << endl;
                    k -= 1;
                    continue;
                }
                else if (nums[i] + nums[j] + nums[k] == 0)
                {
                    cout << "find" << endl;
                    rs.push_back(vector<int>{nums[i], nums[j], nums[k]});
                }
                while (j < nums.size()-1 && nums[j + 1] == nums[j] )
                {
                    cout << "j+1" << endl;
                    j++;
                }
                j += 1;
            }
            while (i < nums.size()-1 && nums[i + 1] == nums[i])
            {
                i++;
            }
            i += 1;
            cout << i << " "  << j << " " << k << endl;
        }
        return rs;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s;
    auto input = new vector<int>{0,0,0,0};
    //auto input = new vector<int>{-1, 0, 1, 2, -1, -4};
    auto rs = s.threeSum(*input);
    for (auto r : rs) {
        for (auto n : r) {
            cout << n << ", ";
        }
        cout << endl;
    }
    return 0;
}

