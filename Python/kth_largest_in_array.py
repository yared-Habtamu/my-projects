class Solution(object):
    def findKthLargest(self, nums, k):
        x=sorted(nums)        
        return x[-k]
           

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
