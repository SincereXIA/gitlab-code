/*
 * @lc app=leetcode.cn id=500 lang=cpp
 *
 * [500] 键盘行
 *
 * https://leetcode-cn.com/problems/keyboard-row/description/
 *
 * algorithms
 * Easy (70.95%)
 * Likes:    177
 * Dislikes: 0
 * Total Accepted:    45K
 * Total Submissions: 60.9K
 * Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
 *
 * 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
 * 
 * 美式键盘 中：
 * 
 * 
 * 第一行由字符 "qwertyuiop" 组成。
 * 第二行由字符 "asdfghjkl" 组成。
 * 第三行由字符 "zxcvbnm" 组成。
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：words = ["Hello","Alaska","Dad","Peace"]
 * 输出：["Alaska","Dad"]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：words = ["omk"]
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：words = ["adsdf","sfd"]
 * 输出：["adsdf","sfd"]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * words[i] 由英文字母（小写和大写字母）组成
 * 
 * 
 */
#include <vector>
#include <string>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> board = {"qwertyuiop", "asdfghjkl", "zxcvbnm" };
        vector<string> result;
        for (auto word : words) {
            int row = -1;
            bool flag = true;
            for (char c : word) {
                if (row != -1) {
                    if (board[row].find(c) != board[row].npos) {
                        continue;
                    }
                    flag = false;
                    break;
                } else {
                    for (int i = 0; i < 3; ++i) {
                        if (board[i].find(c) != board[i].npos) {
                            row = i;
                            continue;
                        }
                    }
                }
            }
            if (flag) {
                result.push_back(word);
            }
        }
        return result;
    }
};
// @lc code=end

