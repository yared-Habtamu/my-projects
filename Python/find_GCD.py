class Solution(object):
    def findGCD(self, nums):
        res=1
        min_element = min(nums)
        i = min_element
        max_element = max(nums)
        while i>1:
            if min_element%i==0 and max_element%i==0:
                return i
            i-=1
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        
