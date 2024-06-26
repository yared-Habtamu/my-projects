class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = []
        for listt in ranges:
            x += [*range(listt[0],listt[1]+1)]
        print(x)
        y = x + [*range(left,right+1)]
        return(set(x)==set(y))
        
