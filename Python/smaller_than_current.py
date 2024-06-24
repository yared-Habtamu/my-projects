class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[]    
        x=sorted(nums)
        for num in nums:
            i=x.index(num)
            ans.append(i)
        return ans
            





        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
