class Solution(object):
    def addSpaces(self, s, spaces):
        res = []
        i, j = 0, 0
        n, m = len(s), len(spaces)
        
        while i < n:
            if j < m and i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(s[i])
            i += 1
        
        return ''.join(res)


