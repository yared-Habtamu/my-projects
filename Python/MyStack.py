class MyStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, x):
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        return None
        """
        :rtype: int
        """
        

    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        return None
        # self.stack.()
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self.stack)>0:
            return False
        return True
        # self.stack.clear()
        """
        :rtype: bool
        """
