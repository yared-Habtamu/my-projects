class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            if nums[len(nums)-1]<target:
                return len(nums)
            if nums[0]>target:
                return 0
            for j in range(len(nums)-1):
                if nums[j]<target and nums[j+1]>target:
                    return j+1            

        i=0
        while i<len(nums):
            if nums[i]==target:
                break
            else:
                i+=1

        return i



        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
