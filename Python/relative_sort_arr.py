class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        ans=[]
        for num in arr2:
            x=arr1.count(num)
            l=[num]*x
            for ln in l:
                ans.append(ln)
        for num in arr1:
            if num not in arr2:
                ans.append(num)
        return ans

        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
