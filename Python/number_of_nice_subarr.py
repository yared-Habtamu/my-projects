class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd = 0
        l = 0
        m = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1

            if odd == k:
                m = l
                while m <= r and nums[m] % 2 == 0:
                    m += 1
                count += (m - l + 1)
                
        return count

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
