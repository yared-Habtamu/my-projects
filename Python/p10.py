class Solution(object):
    def productExceptSelf(self, nums):
        prod = 1
        answer = []
        m = len(nums)
        for j in range(m):
            for i in range(m):
                if j != i:
                    prod = prod * nums[i]
                    if i == m - 1:
                        answer.append(prod)
                        prod = 1
                elif i == j == m - 1:
                    answer.append(prod)
        return answer


