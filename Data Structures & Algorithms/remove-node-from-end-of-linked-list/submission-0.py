# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use slow fast to get code
        # if no fast.next.next it is odd
        # if no fast.next first then it is even
        # then we just count from slow in the middle
        # then we can get size -n + 1
        # then remove / unlink that node


        temp = ListNode()
        temp.next = head
        slow = temp
        fast = temp
        
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return temp.next
            
            

