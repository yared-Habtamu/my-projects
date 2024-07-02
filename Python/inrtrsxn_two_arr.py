class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]
        n1,n2=0,0
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]==nums2[n2]:
                ans.append(nums1[n1])
                n1+=1
                n2+=1
            elif nums1[n1]>nums2[n2]:
                n2+=1
            else:
                n1+=1
        return ans

