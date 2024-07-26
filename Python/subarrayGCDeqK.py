class Solution(object):
    def subarrayGCD(self, nums, k):
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        res = 0
        for i in range(len(nums)):
            small = nums[i]
            for j in range(i, len(nums)):
                if i == j and nums[i] == k:
                    res += 1
                else:
                    small = gcd(small, nums[j])
                    if small < k:
                        break
                    elif small == k:
                        res += 1
        return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
