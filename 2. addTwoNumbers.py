# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        start = ans
        c = 0
        while l1 or l2 or c:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            p = ListNode((num1 + num2 + c) % 10)
            ans.next = p
            c = (num1 + num2 + c) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ans = ans.next
        return start.next
