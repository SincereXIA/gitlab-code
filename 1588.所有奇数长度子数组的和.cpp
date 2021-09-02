/*
 * @lc app=leetcode.cn id=1588 lang=cpp
 *
 * [1588] 所有奇数长度子数组的和
 *
 * https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/description/
 *
 * algorithms
 * Easy (81.90%)
 * Likes:    86
 * Dislikes: 0
 * Total Accepted:    25.2K
 * Total Submissions: 30.8K
 * Testcase Example:  '[1,4,2,5,3]'
 *
 * 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
 * 
 * 子数组 定义为原数组中的一个连续子序列。
 * 
 * 请你返回 arr 中 所有奇数长度子数组的和 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：arr = [1,4,2,5,3]
 * 输出：58
 * 解释：所有奇数长度子数组和它们的和为：
 * [1] = 1
 * [4] = 4
 * [2] = 2
 * [5] = 5
 * [3] = 3
 * [1,4,2] = 7
 * [4,2,5] = 11
 * [2,5,3] = 10
 * [1,4,2,5,3] = 15
 * 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
 * 
 * 示例 2：
 * 
 * 输入：arr = [1,2]
 * 输出：3
 * 解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
 * 
 * 示例 3：
 * 
 * 输入：arr = [10,11,12]
 * 输出：66
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= arr.length <= 100
 * 1 <= arr[i] <= 1000
 * 
 * 
 */

#include <vector>
#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int rs = 0;
        for (size_t i = 0; i < arr.size(); i++)
        {
            for (size_t j = i; j < arr.size(); j++)
            {
                if ( (j-i) % 2 == 0) {
                    //cout << i  << " " << j << endl;
                    int s = 0;
                    for (int k = i; k <= j; k++) {
                        s += arr[k];
                    }
                    rs += s;
                }
            }
        }
        return rs;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution *s = new Solution();
    vector<int> input = {1,4,2,5,3};
    int rs = s->sumOddLengthSubarrays(input);
    cout << rs << endl;
    return 0;
}

