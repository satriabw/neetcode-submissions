# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = self.findMiddle(head)

        # Separate array and reverse the second
        second = middle.next
        middle.next = None
        second = self.reverse(second)

        first = head
        # Merge and reorder
        while first and second:
            tempFirst = first.next
            tempSecond = second.next

            first.next = second
            second.next = tempFirst

            first = tempFirst
            second = tempSecond

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
