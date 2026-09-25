# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # First we need to know reverse point
        # Node before the reverse point and after the reverse point
        # Will help us to connect, but node after reverse point can be referenced later using the reverse algorithm
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        curr = head

        start = 1
        while start != left and curr:
            curr = curr.next
            pre = pre.next
            start += 1
        
        # curr in this case on the position we wanted
        # next we reverse
        prev = None
        steps = right - left + 1
        while steps > 0 and curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

            steps -= 1
        
        end = pre.next
        end.next = curr
        pre.next = prev
        return dummy.next
