class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(1, len(nums)+1):  
            d[i] = 0
        print(d)
        for i in nums:
            d[i] += 1
        print(d)
        result = []
        for key, val in d.items():
            if val == 0:
                result.append(key)
        return result        

        
