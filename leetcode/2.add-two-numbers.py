#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        l3 = head
        carry = 0
        while l1 or l2:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            s = carry + x + y
            carry = s // 10
            l3.next = ListNode(s % 10)
            l3 = l3.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            l3.next = ListNode(carry)

        return head.next

# @lc code=end
