/*
 * @lc app=leetcode.cn id=394 lang=cpp
 *
 * [394] 字符串解码
 *
 * https://leetcode-cn.com/problems/decode-string/description/
 *
 * algorithms
 * Medium (55.18%)
 * Likes:    888
 * Dislikes: 0
 * Total Accepted:    120K
 * Total Submissions: 217.4K
 * Testcase Example:  '"3[a]2[bc]"'
 *
 * 给定一个经过编码的字符串，返回它解码后的字符串。
 * 
 * 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
 * 
 * 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
 * 
 * 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "3[a]2[bc]"
 * 输出："aaabcbc"
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "3[a2[c]]"
 * 输出："accaccacc"
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "2[abc]3[cd]ef"
 * 输出："abcabccdcdcdef"
 * 
 * 
 * 示例 4：
 * 
 * 输入：s = "abc3[cd]xyz"
 * 输出："abccdcdcdxyz"
 * 
 * 
 */
#include <vector>
#include <string>
#include <stack>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    bool isNum(char c) {
        return c >= '0' && c <= '9';
    }
    bool ischar(char c) {
        return c >= 'a' && c <= 'z';
    }
    string make(int time, string s) {
        string rs = "";
        for (int i = 0; i<time; i++) {
            rs += s;
        }
        return rs;
    }

    string decodeString(string s) {
        stack<string> rs;
        stack<int> times;
        stack<string> ss;
        string now = "";
        for (int i = 0; i < s.size();) {
            int c = s[i];
            if (isNum(s[i])) {
                while (isNum(s[i])) {
                    now += s[i];
                    i+= 1;
                }
                int n = stoi(now);
                times.push(n);
                now = "";
                continue;
            }
            if (s[i] == '[') {
                ss.push("[");
                i += 1;
                continue;
            }
            if (ischar(s[i])) {
                while (ischar(s[i])) {
                    now += s[i];
                    i+= 1;
                }
                ss.push(now);
                cout << "ss: " << now << endl;
                now = "";
                continue;
            }
            if (s[i] == ']') {
                int t = times.empty()? 1 : times.top();
                if (!times.empty()){
                    times.pop();
                }
                string r = "";
                while (ss.top()!="[") {
                    r = ss.top() + r;
                    ss.pop();
                }
                ss.pop();
                r = make(t, r);
                ss.push(r);

                cout << "ss: " << r << endl;
                i += 1;
                continue;
            }

        }
        while (!ss.empty()) {
            string r = ss.top();
            ss.pop();
            rs.push(r);
        }
        string result = "";
        while (!rs.empty()) {
            string r = rs.top();
            rs.pop();
            result += r;
        }
        return result;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s;
    auto rs  = s.decodeString("abc3[cd]xyz");
    cout << rs << endl;
    return 0;
}
