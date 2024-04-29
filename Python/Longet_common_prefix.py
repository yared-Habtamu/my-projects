class Solution(object):
    def longestCommonPrefix(self, strs):
        length=[]
        for s in strs:
            length.append(len(s))
        y=min(length)
        ans=""
        slen=len(strs)
        if slen==1:
            return strs[0]
        for j in range(y):
            c=0
            for s in range(slen-1):
                if strs[s][j] ==strs[s+1][j]:
                    c+=1
                    if c==slen-1:
                        ans+=strs[s][j]
                        break
                    s+=1
            else:
                break
        return ans

        """
        :type strs: List[str]
        :rtype: str
        """
        
