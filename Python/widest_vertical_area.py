class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        p2=[i for i,j in points]
        p2.sort()
        ans=0
        for i in range(len(p2)-1):
            if ans<p2[i+1]-p2[i]:
                ans=p2[i+1]-p2[i]
        return ans
