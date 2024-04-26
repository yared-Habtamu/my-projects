 class Solution(object):
    def targetIndices(self, nums, target):
        ind=[]
        x=sorted(nums)
        for i in range(len(nums)):
            if x[i]==target:
                ind.append(i)
        return ind


