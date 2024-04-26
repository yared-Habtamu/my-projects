class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[j]<=nums[j-1]:
                    temp=nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp

#75. Sort Colors  I just use bubble sort approach
