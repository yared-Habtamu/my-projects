
class Solution(object):
    def findAnagrams(self, s, p):
        l='abcdefghijklmnopqrstuvwxyz'
        if len(p)>len(s):
            return []
        d={}
        for x in l:
            d[x]=0
        d1=dict(d)
        d2=dict(d)
        for x in range(len(p)):
            d1[s[x]]+=1
            d2[p[x]]+=1
        l1=[]
        if d1==d2:
            l1=[0]
    
        for x in range(len(p),len(s)):
            d1[s[x]]+=1
            d1[s[x-len(p)]]-=1
            if d1==d2:
                l1.append(x-len(p)+1)
        return l1  
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
