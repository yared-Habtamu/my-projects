class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        c = float('inf')
        left = 0
        window = 0

        for right in range(n):
            window += nums[right]

            while window >= target:
                c = min(c, right - left + 1)
                window -= nums[left]
                left += 1

        return c if c != float('inf') else 0






        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
