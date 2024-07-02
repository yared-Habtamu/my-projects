class Solution:
    def numTimesAllBlue(self, flips):
        prefix_sum = 0
        cur_sum = 0
        ans = 0
        for i in range(len(flips)):
            cur_sum += flips[i]
            prefix_sum += (i + 1)

            if cur_sum == prefix_sum:
                ans += 1
        
        return ans
