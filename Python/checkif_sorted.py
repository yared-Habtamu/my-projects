class Solution:
    def arraySortedOrNot(self, arr, n):
        l=0
        r=1
        #it's parallel variant pointer
        while r<n:
            if arr[l]>arr[r]:
                return 0
            l+=1
            r+=1
        return 1
        
        # code here
