# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            print(head.val)
            if head.next not in s:
                s.add(head.next)
                head = head.next
            else:
                return True
        return False