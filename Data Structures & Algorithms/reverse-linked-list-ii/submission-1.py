# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Find starting, and reverse only up until x steps
        curr = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        # Find starting point
        idx = 1
        while curr.next and idx < left:
            curr = curr.next
            prev = prev.next
            idx += 1
        
        # Reverse
        prevNode = None
        step = right - left + 1
        tail = curr
        while curr and step > 0:
            temp = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = temp
            step -= 1

        prev.next = prevNode
        tail.next = curr
        return dummy.next