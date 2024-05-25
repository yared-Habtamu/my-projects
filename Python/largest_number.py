class Solution(object):
    def largestNumber(self, nums):
        str_nums = map(str, nums)
        print(str_nums)
        sort_rule = lambda x, y : 1 if x + y > y + x else -1
        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(sort_rule), reverse=True)
        if sorted_nums[0] == '0':
            return '0'
        return ''.join(sorted_nums)
   







        """
        :type nums: List[int]
        :rtype: str
        """
        
