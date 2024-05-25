class Solution(object):
    def isValid(self, s):
        stack = []
        bracket = {')': '(', ']': '[', '}': '{'}        
        for ch in s:
            if ch in bracket:
                top_element = stack.pop() if stack else '#'
                if bracket[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        
        return not stack

 
