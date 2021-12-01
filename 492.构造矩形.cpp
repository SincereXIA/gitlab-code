/*
 * @lc app=leetcode.cn id=492 lang=cpp
 *
 * [492] 构造矩形
 *
 * https://leetcode-cn.com/problems/construct-the-rectangle/description/
 *
 * algorithms
 * Easy (55.23%)
 * Likes:    93
 * Dislikes: 0
 * Total Accepted:    36.9K
 * Total Submissions: 61.8K
 * Testcase Example:  '4'
 *
 * 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W
 * 且满足以下要求的矩形的页面。要求：
 * 
 * 
 * 1. 你设计的矩形页面必须等于给定的目标面积。
 * 
 * 2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
 * 
 * 3. 长度 L 和宽度 W 之间的差距应当尽可能小。
 * 
 * 
 * 你需要按顺序输出你设计的页面的长度 L 和宽度 W。
 * 
 * 示例：
 * 
 * 
 * 输入: 4
 * 输出: [2, 2]
 * 解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
 * 但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
 * 
 * 
 * 说明:
 * 
 * 
 * 给定的面积不大于 10,000,000 且为正整数。
 * 你设计的页面的长度和宽度必须都是正整数。
 * 
 * 
 */
#include<vector>
#include<iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> constructRectangle(int area) {
        int low = 1;
        int high = area/2;
        while (low < high)
        {
            int r = low + (high - low) / 2;
            if ((long)r * r < area) {
                low = r + 1;
            } else {
                high = r;
            }
        }
        while (low)
        {
            if (area % low == 0) {
                low = area/low < low ? area/low : low;
                return vector<int>{area / low, low};
            }
            --low;
        }
        return vector<int>{1, 1};
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s;
    auto r = s.constructRectangle(10000000);
    cout << r[0] << endl;
    return 0;
}
