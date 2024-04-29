class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[]    
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    c+=1
            ans.append(c)
            c=0
        
        return ans
            





        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
