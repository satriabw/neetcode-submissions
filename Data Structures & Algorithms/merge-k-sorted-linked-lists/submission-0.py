# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # We can strategize, either using Divide and conquer or a heap queue
        # For the divide and conquer pair each list and then merge accordingly
        # Like a merge sort
        return self.merge(lists)

    
    def merge(self, lists):
        if len(lists) < 1:
            return None
            
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        return self.mergeTwoLists(self.merge(left), self.merge(right))


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
            elif list1:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        return head.next