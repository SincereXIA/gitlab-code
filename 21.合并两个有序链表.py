#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.72%)
# Likes:    1922
# Dislikes: 0
# Total Accepted:    709.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
# 
# 
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        head = ListNode(-1)
        if not l1:
            return l2
        if not l2:
            return l1
        rs = head
        while l1 and l2:
            if l1.val < l2.val:
                rs.next = l1
                l1 = l1.next
            else:
                rs.next = l2
                l2 = l2.next
            print(rs.val)
        if l1:
            rs.next = l1
        if l2:
            rs.next = l2
            
        return head.next
        
            
# @lc code=end

