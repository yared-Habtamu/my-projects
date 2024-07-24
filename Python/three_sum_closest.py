class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return target  
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
                    
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

        return closest_sum
