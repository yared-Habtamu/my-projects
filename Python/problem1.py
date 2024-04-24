class Solution(object):
    def isPalindrome(self, x):
        reverse=0
        num=x
        while x>0:
            remainder = x % 10
            reverse = (reverse * 10) + remainder
            x= x/10
        if reverse==num:
            return True
        else:
            return False 
