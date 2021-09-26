/*
 * @lc app=leetcode.cn id=371 lang=cpp
 *
 * [371] 两整数之和
 *
 * https://leetcode-cn.com/problems/sum-of-two-integers/description/
 *
 * algorithms
 * Medium (58.03%)
 * Likes:    461
 * Dislikes: 0
 * Total Accepted:    58.8K
 * Total Submissions: 99.9K
 * Testcase Example:  '1\n2'
 *
 * 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：a = 1, b = 2
 * 输出：3
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：a = 2, b = 3
 * 输出：5
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * -1000 <= a, b <= 1000
 * 
 * 
 */

// @lc code=start
#include <bitset>

class Solution {
public:
    int subadd(int a, int b, int &co) {
        int s = a ^ b;
        co = a & b;
        return s;
    }
    int add(int a, int b, int c, int &co) {
        int co1;
        int s = subadd(a, b, co1);
        int co2;
        s = subadd(s, c, co2);
        co = co1 | co2;
        return s;
    }
    void print2(int a) {
        std::bitset<32> x(a);
        std::cout << x << '\n';
    }
    int getSum(int a, int b) {
        int i = 0;
        int co = 0;
        int rs = 0;
        unsigned int mask = 1;
        print2(a);
        print2(b);

        while (i < 32)
        {
            cout << "mask: ";
            print2(mask);
            int bita = a & mask;
            int bitb = b & mask;
            co = co << 1;
            cout << "mask "<< mask<< " a: " << bita << " b: " << bitb << " co: " << co << endl;
            int r = add(bita, bitb, co, co);
            rs |= r;
            print2(rs);
            i += 1;
            mask = mask << 1;
        }
        return rs;
    }
};
// @lc code=end

