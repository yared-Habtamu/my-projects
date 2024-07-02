class Solution(object):
    def rotate(self, matrix):
        for arr in matrix:
            arr.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
