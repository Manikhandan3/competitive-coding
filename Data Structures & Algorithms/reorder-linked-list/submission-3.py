# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = prev = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        
        sec = prev
        fir = head
        while sec:
            tmp1, tmp2 = fir.next, sec.next
            fir.next = sec
            sec.next = tmp1
            fir, sec = tmp1, tmp2
