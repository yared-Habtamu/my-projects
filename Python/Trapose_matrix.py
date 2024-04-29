class Solution(object):
    def transpose(self, matrix):
        ans=[]
        for i in range(len(matrix[0])):
            li=[]
            for j in range(len(matrix)):
                li.append(matrix[j][i])
            ans.append(li)
        return ans
