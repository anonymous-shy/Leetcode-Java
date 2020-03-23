/*
 * @lc app=leetcode.cn id=24 lang=java
 *
 * [24] 两两交换链表中的节点
 *
 * https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (64.90%)
 * Likes:    441
 * Dislikes: 0
 * Total Accepted:    84.2K
 * Total Submissions: 129.7K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
 * 
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 * 
 * 
 * 
 * 示例:
 * 
 * 给定 1->2->3->4, 你应该返回 2->1->4->3.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */

// TODO 1.后续使用递归进行运算

// 2. 迭代 没太懂...
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode pre = new ListNode(0);
        pre.next = head;
        ListNode temp = pre;
        while(temp.next != null && temp.next.next != null) {
            ListNode firstNode = temp.next;
            ListNode secondNode = temp.next.next;
            temp.next = secondNode;
            firstNode.next = secondNode.next;
            secondNode.next = firstNode;
            temp = firstNode;
        }
        // Return the new head node.
        return pre.next;
    }
}
// @lc code=end
