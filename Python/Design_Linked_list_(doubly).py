class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

class MyLinkedList(object):
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.num_nodes=0
        # self.head=None
        # self.size=0        

    def get(self, index):
        if index>self.num_nodes-1:
            return -1
        cur=self.head
        while index>=0:
            cur=cur.next
            index-=1
        return cur.val

        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        first_node=self.head.next
        new_node=Node(val,self.head,first_node)
        self.head.next,first_node.prev=new_node,new_node
        self.num_nodes+=1

        """
        :type val: int
        :rtype: None
        """
        
    def addAtTail(self, val):
        last_node=self.tail.prev
        new_node=Node(val,last_node,self.tail)
        self.tail.prev,last_node.next=new_node,new_node
        self.num_nodes+=1

        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        if index>self.num_nodes:
            return
        cur=self.head
        while index>0:
            cur=cur.next
            index-=1
        next_node=cur.next
        new_node=Node(val,cur,next_node)
        cur.next,next_node.prev=new_node,new_node
        self.num_nodes+=1
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        if index>self.num_nodes-1:
            return
        cur=self.head
        while index>0:
            cur=cur.next
            index-=1
        next_node=cur.next.next
        cur.next=next_node
        next_node.prev=cur
        self.num_nodes-=1
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
