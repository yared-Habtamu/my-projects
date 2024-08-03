# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def hasCycle(self, head):
        checked=set()
        cur=head
        while cur:
            if cur in checked:
                return True
            checked.add(cur)
            cur=cur.next
        return False

        
        





        """
        :type head: ListNode
        :rtype: bool
        """
        
