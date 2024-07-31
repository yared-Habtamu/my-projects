class Solution(object):
    def minimumRecolors(self, blocks, k):       
        bs=list(blocks)
        window=bs[:k]
        minimum=window.count('W')
        
        for i in range(len(blocks)-k):
            window.append(bs[k+i])
            window.remove(bs[i])
            minimum=min(minimum,window.count('W'))            
        return minimum





        print(window)
        return 2






        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
