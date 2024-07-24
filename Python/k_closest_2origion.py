class Solution(object):
    def kClosest(self, points, k):
        from math import sqrt
        distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        distances.sort()
        return [point for _, point in distances[:k]]

        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
