# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy
        for _ in range(n):
            cur = cur.next
        temp = dummy
        prev = None
        while cur:
            prev = temp
            cur = cur.next
            temp = temp.next
        prev.next = temp.next
        temp.next = None
        return dummy.next
        