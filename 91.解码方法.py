#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
NUM = 0

def search(s: str) -> int:
    global NUM
    if s == "" :
        NUM += 1
        return 1
    num1 = int(s[0:1])
    if num1 > 0:
        search(s[1:])
    else:
        return 0
    if len(s) < 2:
        return
    num2 = int(s[0:2])
    if num2 > 0 and num2 < 27:
        search(s[2:])
    return 0

D = []
def decode(l: int) -> int:
    global D
    if l ==1 or l == 0:
        return 1
    if D[l] != -1:
        return D[l]
    D[l] = decode(l-1) + decode(l-2)
    return D[l]

def split(s: str):
    pos = [0]
    rs = []
    l = 0
    i = 0
    while i < len(s):
        l += 1
        if s[i] == '0':
            if l-2 < 0:
                return []
            if i >=2:
                rs.append(l-2)
                rs.append(1)
                l = 0
                i += 1
                continue
            elif i == 0:
                return []
            elif i == 1:
                rs.append(1)
                l = 0
                i += 1
                continue
        if i<len(s)-1 and int(s[i:i+2]) > 26:
            rs.append(l)
            l = 0
        i += 1
    if l != 0:
        rs.append(l)
    return rs

class Solution:
    def numDecodings(self, s: str) -> int:
        lens = split(s)
        print(lens)
        if len(lens) == 0:
            return 0
        m = max(lens)
        global D
        for _ in range(m+2):
            D.append(-1)
        rs = 1
        for l in lens:
            rs = rs * decode(l)
        return rs
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("201"))
