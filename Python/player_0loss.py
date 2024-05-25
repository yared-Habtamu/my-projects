class Solution(object):
    def findWinners(self, matches):    
        dic={}
        for x in matches:
            if x[-1] not in dic:
                dic[x[-1]]=1
            else:
                dic[x[-1]]+=1
        temp=set()
        for x in matches:
            if x[0] not in dic:
                temp.add(x[0])
        temp_2=[]
        for x in dic:
            if dic[x]==1:
                temp_2.append(x)
        temp=list(temp)
        res=[]
        temp.sort()
        temp_2.sort()
        res.append(temp)
        res.append(temp_2)
        return res

                        
        
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
