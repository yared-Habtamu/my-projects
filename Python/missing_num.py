class Solution(object):
    def missingNumber(self, nums):
        # x=sum(nums)
        # y=
        n=len(nums)+1
        y=[]
        for i in range(n):
            y.append(i)
        x=sorted(nums)
        for num in y:
            if num not in x:
                return num

        """
        :type nums: List[int]
        :rtype: int
        """
        
