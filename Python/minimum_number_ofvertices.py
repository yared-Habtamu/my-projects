class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        nonRoots = [False] * n
        print(nonRoots)
        for edge in edges:
            nonRoots[edge[1]] = True
        print(nonRoots)
        return [i for i, isNonRoot in enumerate(nonRoots) if not isNonRoot]
        # for i, isNonRoot in enumerate(nonRoots):
        #     if not isNonRoot:
        #         return nonRoots.index()
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
