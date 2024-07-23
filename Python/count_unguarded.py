class Solution:
    def countUnguarded(self, m: int, n: int, g: List[List[int]], w: List[List[int]]) -> int:
        ans = []
        arr=[[[-1,-1]]*(n) for i in range(m)]
        for i,j in w:
            arr[i][j] = ["w","w"]
        g.sort()
        for i,j in g:
            p,q = i,j
            r,s = i,j
            while(p<m and arr[p][j][0]!="w" and arr[p][j][1]!="r"):
                arr[p][j] = [1,"r"]
                p+=1
            while(q<n and arr[i][q][0]!="w" and arr[i][q][1]!="d"):
                arr[i][q] = [1,"d"]
                q+=1
            while(r>=0 and arr[r][j][0]!="w" and arr[r][j][1]!="l"):
                arr[r][j] = [1,"l"]
                r-=1
            while(s>=0 and arr[i][s][0]!="w" and arr[i][s][1]!="u"):
                arr[i][s] = [1,"u"]
                s-=1
        ans=0
        for i in range(m):
            for j in range(n):
                if arr[i][j]==[-1,-1]:
                    ans+=1
        return ans
      
