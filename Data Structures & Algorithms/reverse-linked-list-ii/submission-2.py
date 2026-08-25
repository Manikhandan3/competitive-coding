# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0,head)
        cur = prev = dummy
        for _ in range(left):
            prev = cur
            cur = cur.next
        prev.next = None
        s = second = cur
        for _ in range(right-left):
            second = second.next
        third = second.next
        second.next = p = None
        while cur:
            temp = cur.next
            cur.next = p
            p = cur
            cur = temp
        prev.next = p
        s.next = third
        return dummy.next
        
        