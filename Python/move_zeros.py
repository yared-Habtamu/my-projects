class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder,seeker=0,0
        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[holder],nums[seeker]=nums[seeker],nums[holder]
                holder+=1
            seeker+=1
