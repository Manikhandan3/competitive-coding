# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.front = self.rear = None

    def enQueue(self, value: int) -> bool:
        if not self.capacity:
            return False
        if not self.front:
            self.front = ListNode(value)
            self.rear = self.front
        else:
            self.rear.next = ListNode(value)
            self.rear = self.rear.next
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.front:
            self.capacity += 1
            self.front= self.front.next
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.front:
            return self.front.val
        return -1

    def Rear(self) -> int:
        if self.front:
            return self.rear.val
        return -1

    def isEmpty(self) -> bool:
        if self.front:
            return False
        return True

    def isFull(self) -> bool:
        return not self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()