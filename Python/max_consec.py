class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        left, right = 0, 0
        n = len(nums)
        ans = 0
        curr_sum = 0
        while right < n:
            if nums[right] == 0:
                zero_count += 1
                while left<=right and  zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    curr_sum -=1 
                    left += 1
            curr_sum += 1
            ans = curr_sum if curr_sum > ans else ans 
            right += 1
            
        return ans



        
