class Solution(object):
    def maximumUniqueSubarray(self, nums):
        slow = 0
        fast = 0
        tot = 0
        max_tot = 0
        window = set()

        while fast < len(nums):
            if nums[fast] not in window:
                window.add(nums[fast])
                tot += nums[fast]
                max_tot = max(max_tot, tot)
                fast += 1
            else:
                window.remove(nums[slow])
                tot -= nums[slow]
                slow += 1

        return max_tot

        """
        :type nums: List[int]
        :rtype: int
        """
