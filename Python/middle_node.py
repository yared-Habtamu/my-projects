# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution(object):
    def middleNode(self, head):
        slow=head
        fast=head
        while  fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
