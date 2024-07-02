class Solution(object):
    def reductionOperations(self, nums):
        nums.sort(reverse=True)
        ans=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                ans+=i+1
        return ans         
       

        
        """
        :type nums: List[int]
        :rtype: int
        """
        
