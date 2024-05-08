class Solution(object):
    def applyOperations(self, nums):
        ans=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                x=nums[i]*2
                ans.append(x)
                nums[i+1]=0
            else:
                ans.append(nums[i])
            if i==len(nums)-2:
                ans.append(nums[-1])
                
        ret=[n for n in ans if n!=0]+[0]*ans.count(0)
        return ret

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
