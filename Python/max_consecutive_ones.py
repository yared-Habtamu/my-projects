class Solution(object):
    def longestOnes(self, nums, k):
        from collections import deque

        temp = deque()
        i=0
        j = len(nums)
        count=0
        maxlen = 0
        
        while i<j:
            if nums[i]==0:
                count+=1
            temp.append(nums[i])
            if count>k:
                maxlen = max(len(temp)-1,maxlen)
            while count>k:
                if temp[0]==0:
                    count-=1
                temp.popleft()
            i+=1
        return max(len(temp),maxlen)
