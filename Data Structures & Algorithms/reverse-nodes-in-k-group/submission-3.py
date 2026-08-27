# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findK(node):
            for _ in range(k-1):
                if not node:
                    break
                node = node.next
            return node
        
        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        
        res = ListNode(-1,head)
        groupPrev = res
        groupNext = groupPrev.next
        while groupNext:
            kth = findK(groupNext)
            if not kth:
                return res.next
            groupNext = kth.next
            kth.next = None
            temp = groupPrev.next
            groupPrev.next = reverse(temp)
            temp.next = groupNext
            groupPrev = temp
        return res.next
