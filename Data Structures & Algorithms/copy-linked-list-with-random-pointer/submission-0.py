"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        curr = head

        newhead = Node(0)
        newcurr = newhead

        while curr:
            node = Node(x=curr.val)
            copy[curr] = node

            newcurr.next = node
            newcurr = newcurr.next
            curr = curr.next
        
        newcurr = newhead.next
        curr = head

        while newcurr and curr:
            if curr.random in copy:
                newcurr.random = copy[curr.random]
            curr = curr.next
            newcurr = newcurr.next

        return newhead.next
        
            
        