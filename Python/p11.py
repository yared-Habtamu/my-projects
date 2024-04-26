class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1a = [0] * (m+n)
        for i in range(m):
            nums1a[i] = nums1[i]
        ind2 = 0
        ind1a = 0
        for ind1 in range(m+n):
            if ind1a == m:
                nums1[ind1] = nums2[ind2]
                ind2 += 1
            elif ind2 == n:
                nums1[ind1] = nums1a[ind1a]
                ind1a += 1
            elif nums1a[ind1a] <= nums2[ind2]:
                nums1[ind1] = nums1a[ind1a]
                ind1a += 1
            else:
                nums1[ind1] = nums2[ind2]
                ind2 += 1
    #88, Merge sorted list
