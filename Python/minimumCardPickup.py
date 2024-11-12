class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        l = 0
        res = float('inf')
        d = {}

        for right in range(len(cards)):

            if cards[right] not in d:
                d[cards[right]] = 1
            else:
                d[cards[right]] += 1

            if d[cards[right]] == 2:

                while cards[l] != cards[right]:
                    d[cards[l]] -= 1
                    l += 1

                res = min(res, right-l+1)

                d[cards[right]] -= 1
                l += 1

        if res != float('inf'):
            return res
        return -1      
