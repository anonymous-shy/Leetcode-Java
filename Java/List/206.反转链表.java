/*
 * @lc app=leetcode.cn id=206 lang=java
 *
 * [206] 反转链表
 *
 * https://leetcode-cn.com/problems/reverse-linked-list/description/
 *
 * algorithms
 * Easy (67.78%)
 * Likes:    852
 * Dislikes: 0
 * Total Accepted:    192.6K
 * Total Submissions: 282.8K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 反转一个单链表。
 * 
 * 示例:
 * 
 * 输入: 1->2->3->4->5->NULL
 * 输出: 5->4->3->2->1->NULL
 * 
 * 进阶:
 * 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // 定义两个节点变量
        // 1. 前指针节点
        ListNode prev = null;
        // 2. 当前指针节点
        ListNode curr = head;
        // 3. 初始化临时节点
        ListNode nextTmp = null;
        while (curr != null) {
            // 使用临时节点存储当前节点的下一个节点
            nextTmp = curr.next;
            // 当前节点的前一个指向下一个节点
            curr.next = prev;
            // 前节点与当前节点互换
            prev = curr;
            // curr后移,等于next
            curr = nextTmp;
        }
        return prev;
    }
}
// @lc code=end
