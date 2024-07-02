class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[]
        for i in range(2*n):
            if i<=n-1:
                ans.append(nums[i])
            else:
                ans.append(nums[i-n])
        return ans
