# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        prev = slow.next = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        cur = head
        while prev:
            temp1, temp2 = cur.next, prev.next
            cur.next = prev
            prev.next = temp1
            cur = temp1
            prev = temp2
