# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head):
        def reverse(h):
            prev = None
            while h:
                nxt = h.next
                h.next = prev
                prev = h
                h = nxt
            return prev

        head = reverse(head)
        mx = 0
        curr = head
        prev = None

        while curr:
            if curr.val >= mx:
                mx = curr.val
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        return reverse(head)