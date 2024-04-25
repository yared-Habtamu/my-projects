class Solution(object):
    def maxArea(self, height):
        maxa = 0
        l = 0
        r = len(height) - 1

        while l < r:
            if height[l]<height[r]:
                h=height[l]
            else:
                h=height[r]
            w = r - l
            area = h * w
            if maxa<area:
                maxa=area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxa

#Leet Code 11, Container with most water 
