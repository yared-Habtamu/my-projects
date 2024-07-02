class Solution(object):
    def validMountainArray(self, arr):
        x=max(arr)
        i=arr.index(x)
        if len(arr)<3 or i==len(arr)-1 or i==0:
            return False
        for k in range(i):
            if arr[k]>=arr[k+1]:
                return False
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[j-1]:
                return False
        return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        
