class Solution(object):
    def isPalindrome(self, s):
        li=[]
        for i in range(len(s)):
            if s[i].isalpha():
                x=s[i].lower()
                li.append(x)
            if s[i].isdigit():
                li.append(s[i])

        print(li)
        l,r=0,len(li)-1
        while l<r:
            if li[l]!=li[r]:
                return False
            l+=1
            r-=1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
