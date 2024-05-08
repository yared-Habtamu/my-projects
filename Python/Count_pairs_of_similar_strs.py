class Solution(object):
    def similarPairs(self, words):
        c=0
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    x=set(words[i])
                    y=set(words[j])
                    if x==y:
                        c+=1
        return c/2
        """
        :type words: List[str]
        :rtype: int
        """
        
