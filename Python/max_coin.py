class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        tot = len(piles) // 3
        i = len(piles) - 2
        res = 0
        
        while tot > 0:
            res += piles[i]
            i -= 2
            tot -= 1
        
        return res




        """
        :type piles: List[int]
        :rtype: int
        """

