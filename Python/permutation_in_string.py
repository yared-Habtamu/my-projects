class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
            
        s1_cnt,s2_cnt=[0]*26,[0]*26
        for i in range(len(s1)):
            s1_cnt[ord(s1[i])-ord('a')]+=1
            s2_cnt[ord(s2[i])-ord('a')]+=1
        
        same=0
        for i in range(26):
            if s1_cnt[i]==s2_cnt[i]:
                same+=1
        
        delete=0
        for add in range(len(s1),len(s2)):
            if same==26:
                return True
            ind=ord(s2[add])-ord('a')
            s2_cnt[ind]+=1
            if s1_cnt[ind]==s2_cnt[ind]:
                same+=1
            elif s1_cnt[ind]+1==s2_cnt[ind]:
                same-=1

            ind=ord(s2[delete])-ord('a')
            s2_cnt[ind]-=1
            if s1_cnt[ind]==s2_cnt[ind]:
                same+=1
            elif s1_cnt[ind]-1==s2_cnt[ind]:
                same-=1
            delete+=1
        return same==26



        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
