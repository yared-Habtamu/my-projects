class Solution(object):
    def findMaxAverage(self, nums, k):
        start = 0
        end = 0
        n = len(nums)
        sum = 0
        max_avg = float('-inf')
        while end < n:
            if k>(end-start):
                sum += nums[end]
            if k==(end-start+1):
                max_avg = max(max_avg,sum)
                sum -= nums[start]
                start+=1
            end+=1
        return max_avg/float(k)

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
