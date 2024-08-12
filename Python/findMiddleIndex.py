class Solution(object):
    def findMiddleIndex(self, nums):
        left,right=0,0
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            if left==right:
                return i
            if i==len(nums)-2:
                left=sum(nums[:i+1])
                if left==0:
                    return len(nums)-1
                break
        return -1


        """
        :type nums: List[int]
        :rtype: int
        """
        
