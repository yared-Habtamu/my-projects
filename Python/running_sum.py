class Solution(object):
    def runningSum(self, nums):
        ans=[nums[0]]
        s=nums[0]
        for i in range(1,len(nums)):
            s+=nums[i]
            ans.append(s)
        return ans
        
