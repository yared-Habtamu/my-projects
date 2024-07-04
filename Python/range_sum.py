class NumArray(object):

    def __init__(self, nums):
        self.nums=nums

        """
        :type nums: List[int]
        """
        
    def sumRange(self, left, right):
        s=sum(self.nums[left:right+1])
        return s
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
