# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans

        carry = 0
        while l1 or l2:

            v1 = getattr(l1, "val", 0)
            v2 = getattr(l2, "val", 0)

            total = v1 + v2 + carry
            digit, carry = total % 10, total // 10

            node = ListNode(val=digit)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            node = ListNode(val=carry)
            curr.next = node
        
        return ans.next
        