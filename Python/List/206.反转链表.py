#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (67.78%)
# Likes:    852
# Dislikes: 0
# Total Accepted:    192.6K
# Total Submissions: 282.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点, pre和cur, pre指向None
        prev = None
        curr = head
        # 遍历链表
        while curr:
            # 临时记录当前节点的next
            tmp = curr.next
            # 当前节点的next反向指到prev
            curr.next = prev
            # pre和cur节点都前进一位
            # 前节点与当前节点互换
            prev = curr
            # curr后移,等于next
            curr = tmp
        return prev
# @lc code=end

